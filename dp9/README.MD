### About my project
---
* **作业1:** 识别身份证号码
    * 文件: re_ID_num.py, area.json
        * 样例输入: `please input your ID num:411628200010033432`
        * 样例输出: `(True, '河南省 周口市 鹿邑县')`
        * 如果输入的身份证号码不正确，会返回相应的错误信息，包括:
            * 长度错误
            * 格式错误(包含错误字符)
            * 地区码(前六位)错误
            * 日期格式错误
            * 校验码错误
        * `area.json`文件用于存储地区码字典信息
        * **注意** 经过测试发现在网上找的身份证号码测试不能通过，因为以前的地区码已经发生变化，即使身份证号码正确也会报错`Area 
        Code Error`测试时最好选择20岁左右的人的身份证号码进行测试。
---
* **作业2:** 网络编程实现timestamp到格式化时间的转换
    * 文件: TCP_Client.py, TCP_Server.py, client.py, server.py
        * TCP_Client.py, TCP_Server.py
            * client每隔10秒向server发送当前时间戳
            * server收到后将其转化成格式化的时间并发送给client
---
* **作业3** 网络爬虫爬取邮箱并发送邮件
    * 文件: Christmas.html, Christmas1.jpg, selenium_email.py, send_email.py, 
    teacher_email.py
        * selenium_email.py使用selenium库实现直接爬取邮箱信息，速度较慢，需要配置环境
        * teacher_email.py使用常规方法requests库对网页html信息进行处理得到邮箱
        * send_email.py实现发送邮件功能
            * 其中Christmas.html和Christmas.jpg是用来发送的邮件内容，本来是想圣诞节发给老师，模仿各种广告邮件，发送制作比较好看的邮件(html格式)，结果太忙就忘了
        * **注意**： 如果运行selenium_email.py和teacher_email.py会向软件学院老师邮箱发送邮件
        
            