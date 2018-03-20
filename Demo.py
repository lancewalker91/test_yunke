'''import smtplib
from email.mime.text import MIMEText
from email.header import Header
smtpserver = 'smtp.exmail.qq.com'
user = 'litao@litao.ink'
password = 'Lt639607'
sender = 'litao@litao.ink'
receiver = 'litao@yunke.com'
subject = 'python email test'
msg = MIMEText('<html><h1>您好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

smtp =smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()'''
