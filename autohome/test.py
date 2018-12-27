from bs4 import BeautifulSoup
import requests


article_url = "https://www.autohome.com.cn/advice/201812/927318.html"
article_html = requests.get(article_url)
article_soup = BeautifulSoup(article_html.text, "html.parser")
article_content = article_soup.find("div", class_="container article")
if article_content:
    time_span = article_content.find("div", class_="article-info").find("span", class_="time")
    time = time_span.get_text()
    print(time)
    article_content_div = article_content.find("div", id="articleContent")
    for content in article_content_div.find_all("p"):
        if content.get_text():
            print(content.get_text())
        else:
            img = content.find("a").find("img")
            print("\t图片: ", f"<{img['title']}> ", "https:" + img["src"])
    article_comment_span = article_content.find("div", "article-tools").find("span", class_="comment")
    article_comment_url = "https:" + article_comment_span.find("a")["href"]
    print(article_comment_url)
    article_comment_html = requests.get(article_comment_url)
    article_comment_soup = BeautifulSoup(article_comment_html.text, "html.parser")
    article_comment_list = article_comment_soup.find("div", class_="content").find("dl", id="reply-list")
    print(article_comment_list)
    users = article_comment_list.find_all("dt")
    user_comments = article_comment_list.find_all("dd")
    print(len(users), len(user_comments))
else:
    article_content = article_soup.find("div", class_="wrap article-album")
    if article_content:
        pass

# html = requests.get(url="https://www.autohome.com.cn/2098/#levelsource=000000000_0&pvareaid=101594")
# # with open("test.txt", "w+", encoding="utf8") as f:
# #     f.write(html.text)
# soup = BeautifulSoup(html.text, "html.parser")
# art = soup.find("div", class_="athm-sub-nav__channel athm-js-sticky").find_all("li")
# part_url = art[6].find("a")["href"]
#
# article_url = "https://www.autohome.com.cn" + part_url
# right_pos = article_url.rfind("/")
# article_url = article_url[:right_pos+1]
# print(article_url)
# article_html = requests.get(article_url)
# article_soup = BeautifulSoup(article_html.text, "html.parser")
# page_info = article_soup.find("div", class_="page")
# page_num = 1
# if page_info:
#     pages = page_info.find_all("a", target="_self")
#     page_num = int(pages[-2].get_text())
#     print(page_num)
#
# for i in range(1, page_num+1):
#     if i==1:
#         page_url = article_url
#     else:
#         page_url = article_url[:-4] + str(i) + article_url[-3:]
#     print(f"正在查找第{i}页的文章", page_url)
#     page_html = requests.get(page_url)
#     page_soup = BeautifulSoup(page_html.text, "html.parser")
#     articles = page_soup.find("div", class_="cont-info").find_all("li")
#     for article in articles:
#         each_article = article.find("h3").find("a")
#         each_article_url = "https:" + each_article["href"]
#         each_article_title = each_article.get_text()
#         print("\t", each_article_title, "\t", each_article_url)
