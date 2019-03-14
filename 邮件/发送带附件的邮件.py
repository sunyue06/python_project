import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender='yue_sun@chinacache.com'     #发件人
psd='qazWSX123.'                     #授权码
receiver='18553358533@163.com'        #收件人



subject='逸云资源' #主题
#创建带附件的实例
msg=MIMEMultipart()
msg['Subject']=Header(subject,'utf-8')
msg['from']=Header(sender,'utf-8')
msg['To']=receiver

#创建正文，把文本添加到msg类中
msg.attach(MIMEText('逸云节点资源，请查看附件','plain','utf-8'))

#构造附件
file_path='C:/Users/yue.sun/Desktop/自己/py/工作/逸云节点.xls'
att1=MIMEText(open(file_path,'rb').read(),
              'base64','utf-8')
att1["Content-Type"]='application/octet-stream;name=%s'%Header(file_path,'utf-8').encode('utf-8')
att1["Content-Disposition"]='attachment;file_name=%s'%Header('逸云节点.xls','utf-8').encode('utf-8')
msg.attach(att1)

smtp=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
#smtp.connect('smtp.exmail.qq.com',465)
smtp.login(sender,psd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()