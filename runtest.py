import time
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    att = MIMEText(mail_body,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attacment;filename = "test_yunke_report.html"'
    msgRoot = MIMEMultipart('related')
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msgRoot.attach(att)
    msgRoot.attach(msg)
    msgRoot['Subject'] = Header('云课自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('mail.yunke.com')
    smtp.login('litao@yunke.com','litao12')
    smtp.sendmail('litao@yunke.com',['litao@yunke.com'],msgRoot.as_string())
    smtp.quit()
    print('email has been send out!')
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn:os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = r'C:\Users\Administrator\Desktop\test_yunke'
    test_report = r'D:\data\test_yunke'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open( test_report + '\\' + now + '云课登录测试报告.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='云课UI自动化测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_email(new_report)#发送测试报告