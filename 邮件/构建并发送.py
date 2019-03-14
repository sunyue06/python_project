import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host='smtp.163.com'
mail_user='18553358533@163.com'
mail_password='qweASD123'
sender='18553358533@163.com'
receiver='835448967@qq.com'

msg=MIMEMultipart('mixed')
#message=MIMEText('逸云节点资源','plain','utf-8')
msg['From']=sender
msg['To']=receiver
msg['Subject']='逸云资源'
msg.attach('逸云节点资源')
file_path='C:/Users/yue.sun/Desktop/自己/py/工作/逸云节点.xls'
with open(file_path,'rb') as fp:
    mail_body=fp.read()
file=MIMEText(mail_body,'base64','utf-8')
file["Content-type"]=('application/octet-stream')
file["Content-Disposition"]=('attachment;filename="逸云资源.xls"')
file.add_header('Content-ID','<0>')
file.add_header('X-Attachment-Id', '0')
msg.attach(file)

smtp=smtplib.SMTP()
smtp.connect(mail_host)
smtp.login(mail_user,mail_password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

