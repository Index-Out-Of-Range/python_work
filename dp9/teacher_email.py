import requests
import re
from bs4 import BeautifulSoup

url = 'http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52?start=10'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
}
html = requests.get(url, headers)

soup = BeautifulSoup(html.text, "html.parser")

info_span = soup.find_all("div", class_="span9")

for info in info_span[1:]:
    name = info.find("a").get_text()
    span = info.find("span", class_="cloaked_email")
    info_list = str(span).replace("\">", "\"").split()
    email_list = []
    email1 = email2 = ""
    for x in info_list:
        if re.match(r"^data-ep-\w{5}=\".*\".*$", x):
            email_list.append(x)
    for i in range(len(email_list)):
        left = email_list[i].find("\"")
        right = email_list[i].rfind("\"")
        if i % 2 == 0:
            email1 += email_list[i][left+1:right]
        elif i % 2 == 1:
            email2 = email_list[i][left+1:right] + email2
    print(name, ":", email1+email2)


