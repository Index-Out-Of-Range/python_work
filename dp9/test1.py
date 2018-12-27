# from time import *
#
# tm = time()
#
# print(gmtime(tm))
# print(localtime(tm))
#
# import os
#
# def walk(dir_name):
#     for name in os.listdir(dir_name):
#         path = os.path.join(dir_name, name)
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)
#
# walk('.')

# from time import *
# import re
# t = time()
# print(t)
# lt = localtime(t)
# print(lt)
# ft = strftime("%Y %m %d %H:%M:%S", lt)
# print(ft)
# st = strptime(ft, "%Y %m %d %H:%M:%S")
# print(st)
# ts = mktime(st)
# print(ts)
#
# print(re.match(r'''^"$''', "\""))
# print(r'''"''')

# def run(a, *args):
#     print(a)
#     print(args)
#     print("对args拆包: ", *args)
#     print("将未拆包的数据传给run1")
#     run1(args)
#     print("将拆包后的数据传给run1")
#     run1(*args)
#
# def run1(*args):
#     print("输出元组: ", args)
#     print("对元组进行拆包: ", *args)
#
# run(1, 2, 3)
#
# def run(**kwargs):  # 传来的 key = value 类型的实参会映射成kwargs里面的键和值
#     # kwargs是一个字典，将未命名参数以键值对的形式
#     print(kwargs)
#     print("对kwargs拆包")
#     #  此处可以把**kwargs理解成对字典进行了拆包，{"a":1,"b":2}的kwargs字典又
#     # 被拆成了a=1,b=2传递给run1,但是**kwargs是不能像之前*args那样被打印出来看的
#     run1(**kwargs)
#     # print(**kwargs)
#
#
# def run1(a, b):  # 此处的参数名一定要和字典的键的名称一致
#     print(a, b)
#
#
# run(a=1, b=2)

# import requests
# import re
# from bs4 import BeautifulSoup

# url = 'http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52?start=10'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
# }
# html = requests.get(url, headers)

# soup = BeautifulSoup(html.text, "html.parser")

# info_span = soup.find_all("div", "span9")

# for info in info_span[1:]:
#     print(info)
#     print("-"*50)

