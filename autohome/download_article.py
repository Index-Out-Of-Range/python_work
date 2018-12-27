# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import random
import re


def get_all_cars(main_url, file_path):
    html = requests.get(main_url)
    soup = BeautifulSoup(html.text, "html.parser")
    catalog = soup.find("div", id="hotcar-1").find_all("div", class_="name")

    for cata in catalog:
        # suv, 紧凑型车, 中型车
        cata_a = cata.find("a")
        print(cata_a["href"])
        print(cata_a.get_text())
        car_url = main_url + cata_a["href"]
        car_html = requests.get(car_url)
        car_soup = BeautifulSoup(car_html.text, "html.parser")
        # 有4个 class_="tab-content-item"
        car_letter_boxes = car_soup.find("div", class_="tab-content-item").find_all("div", class_="uibox")
        for car_letter_box in car_letter_boxes[:]:
            # 车牌按字母排序 A~Z, 一个字母下有很多车牌, 对每个字母进行处理
            car_brand_info = car_letter_box.find("div", class_="uibox-con rank-list rank-list-pic")
            if car_brand_info:
                car_brands = car_brand_info.find_all("dl", olr=re.compile("^.*$"))
                for car_brand in car_brands:
                    # 一个车牌有很多种车型, 对每个车牌进行处理
                    brand_name = car_brand.find("div").find("a").get_text()
                    print("-car brand-", brand_name)
                    car_name_lists = car_brand.find_all("ul", class_="rank-list-ul")
                    for car_name_list in car_name_lists:
                        car_name_lis = car_name_list.find_all("li", id=re.compile("^.*$"))
                        for car_name_li in car_name_lis:
                            car_a_tag = car_name_li.find("h4").find("a")
                            specific_car_url = "https:" + car_a_tag["href"]
                            print("\t", car_a_tag.get_text(), specific_car_url)
                            # 至此, 找到了每一辆车的url, 需要从这个url中找到它对应的一系列文章
                            get_each_car_articles(main_url, specific_car_url)
            else:
                continue


def get_each_car_articles(main_url, specific_car_url):
    # 传入的是每一种车的url, 即specific_car_url
    specific_car_html = requests.get(url=specific_car_url)
    specific_car_soup = BeautifulSoup(specific_car_html.text, "html.parser")
    art = specific_car_soup.find("div", class_="athm-sub-nav__channel athm-js-sticky").find_all("li")
    part_url = art[6].find("a")["href"]
    specific_car_article_url = main_url + part_url

    right_pos = specific_car_article_url.rfind("/")
    specific_car_article_url = specific_car_article_url[:right_pos + 1]
    specific_car_article_html = requests.get(specific_car_article_url)
    specific_car_article_soup = BeautifulSoup(specific_car_article_html.text, "html.parser")
    page_info = specific_car_article_soup.find("div", class_="page")
    page_num = 1
    if page_info:
        pages = page_info.find_all("a", target="_self")
        page_num = int(pages[-2].get_text())

    for i in range(1, page_num + 1):
        if i == 1:
            page_url = specific_car_article_url
        else:
            page_url = specific_car_article_url[:-4] + str(i) + specific_car_article_url[-3:]
        print("\t"*2, f"正在查找第{i}页的文章", page_url)
        page_html = requests.get(page_url)
        page_soup = BeautifulSoup(page_html.text, "html.parser")
        articles = page_soup.find("div", class_="cont-info").find_all("li")
        for article in articles:
            each_article = article.find("h3").find("a")
            each_article_url = "https:" + each_article["href"]
            each_article_title = each_article.get_text()
            print("\t"*3, each_article_title, "\t", each_article_url)
            dowload_each_article(each_article_url)


def dowload_each_article(each_article_url):
    each_article_html = requests.get(each_article_url)



if __name__ == '__main__':
    main_url = "https://www.autohome.com.cn"
    main_path = "D:\pycharm\python_work\autohome\汽车之家"
    # url = "https://www.autohome.com.cn/tianjin/"
    get_all_cars(main_url, main_path)