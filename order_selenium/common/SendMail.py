import requests
import unittest
from order_selenium.common.HTMLTestRunner import HTMLTestRunner
from lxml.html._diffcommand import description
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(report_file):
        # 读取测试报告内容
    f = open(report_file, 'rb')
    content = f.read().decode('utf-8')
#    print(content)
    f.close()
#     content = '第一封邮件'
 
    msg = MIMEMultipart('mixed')
#     print(type(msg))
        # 添加邮件内容

    #邮件正文内容
    mail_content = '''
                  <p>Python 邮件发送测试报告</p>
                  <p><a href='http://www.baidu.com'></p>
                  '''  
    
    msg_html = MIMEText(mail_content, 'html', 'utf-8') #邮件正文内容及格式
#     print(type(msg_html))
#     print(msg_html)
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = '本邮件为自动发送，请勿回复'
    msg['From'] = '王晓文<wangxiaowen@zhongruigroup.com>'
    msg['To'] = '王晓文<15092286618@qq.com>'

    tolist = ['wangxiaowen@zhongruigroup.com', '15092286618@qq.com','wxyzwen@163.com']
    
    try:
        # 连接服务器
        s = smtplib.SMTP('smtp.qiye.163.com', 25)
        # 登陆
        s.login('wangxiaowen@zhongruigroup.com', '1qaz@WSX')
        # 发送邮件
        s.sendmail('wangxiaowen@zhongruigroup.com', tolist, msg.as_string())
        s.quit()
        print('发送成功！')
    except Exception as e:
        print("Exceptioin ", e)
        print('发送失败！')

