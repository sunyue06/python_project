import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.application import MIMEApplication

#设置参数
smtpserver = 'smtp.163.com'
username = '18553358533@163.com'
password='qweASD123'
sender='18553358533@163.com'
#收件人信息
receiver='835448967@qq.com'

subject='Python Post test'
msg=MIMEMultipart('mixed')
msg['Subject']=subject
msg['From']=sender
msg['To']=receiver
#msg['Date']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#构建文字内容
text='逸云资源，详情见附件'
text_plain=MIMEText(text,'plain','utf-8')#
msg.attach(text_plain)


name=MIMEApplication(open('C:/Users/yue.sun/Desktop/自己/py/工作/逸云节点.xls','rb').read())
name.add_header('Content-Disposition', 'attachment', file_name='C:/Users/yue.sun/Desktop/自己/py/工作/逸云节点.xls')
name.add_header('Content-ID','<0>')
name.add_header('X-Attachment-Id', '0')
msg.attach(name)


#发送邮件
smtp=smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
