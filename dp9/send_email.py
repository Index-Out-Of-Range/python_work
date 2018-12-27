from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_emails(from_addr, name, to_addr):
    password = "sszslrswoaoaeaaa"
    smtp_server = "smtp.qq.com"

    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    with open('D:\pycharm\python_work\dp9\Christmas1.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpg', filename='Christmas1.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment',
                        filename='Christmas1.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    with open("D:\pycharm\python_work\dp9\Christmas.html", "r", encoding="utf-8") as f:
        content = f.read()
    msg.attach(MIMEText(content, 'html', 'utf-8'))
    msg['From'] = _format_addr('一位不愿透露姓名的靓仔 <%s>' % from_addr)
    msg['To'] = _format_addr(f'{name} <%s>' % to_addr)
    msg['Subject'] = Header('圣诞节快乐!', 'utf-8').encode()

    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.starttls()
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("success!")
    except Exception as e:
        print("failed!")
        print(e)


if __name__ == '__main__':
    # receiver_dict = {"丁鹏谷歌": "dp1612841@gmail.com", "丁鹏QQ": "1913765060@qq.com"}
    receiver_dict = {"CYP": "717678696@qq.com"}
    from_addr = "2332939290@qq.com"
    for key, value in receiver_dict.items():
        send_emails(from_addr, key, value)