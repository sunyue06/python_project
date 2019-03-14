import requests
import json
import xlwt
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

a=''
filename1=''
msg=''
#sender='18553358533@163.com'     #发件人
#psd='qweASD123'                     #授权码
#receiver='jianjie.ma@chinacache.com','yatao.li@chinacache.com'       #收件人
#subject='逸云资源' #主题
def make_dir():
    global a
    key='Date'
    value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data ={'Authorization':'CC95AC02F3D28EA2B848258BE87F88F8',
           'Content-Type':'json'}
    data[key]=value
    response=requests.get('http://openapi.exclouds.com/contentService/QueryCacheIp?domain=*.9iwuli.com&detail=Y',
                          headers=data)
    jd=json.loads(response.text)
    a=(jd['results'])

def make_excel():
    global filename1
    num = 0
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('逸云资源')
    for i in a:

        worksheet.write(num, 0, label=i['ip'])
        worksheet.write(num, 1, label=i['isp'])
        worksheet.write(num, 2, label=i['pro'])
        num+=1
        workbook.save('逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d'))
        filename1 ='逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d')

def make_eamil(subject,sender,receiver):
    global msg
    #创建带附件的实例
    msg=MIMEMultipart()
    msg['Subject']=Header(subject,'utf-8')
    msg['from']=Header(sender,'utf-8')
    msg['To']=receiver
    #创建正文，把文本添加到msg类中
    msg.attach(MIMEText('逸云节点资源，请查看附件','plain','utf-8'))
    #构造附件
    file_path='C:/Users/yue.sun/Desktop/自己/py/工作/%s'%filename1
    att1=MIMEText(open(file_path,'rb').read(),
                  'base64','utf-8')
    #att1["Content-Type"]='application/octet-stream;name=%s'%Header(filename,'utf-8').encode('utf-8')
    #att1["Content-Disposition"]='attachment;file_name=%s'%Header('%s'%filename,'utf-8').encode('utf-8')
    att1.add_header('Content-Disposition', 'attachment', filename=filename1)
    att1.add_header('Content-ID', '<0>')
    att1.add_header('X-Attachment-Id', '0')
    msg.attach(att1)

def send_email(mail_host,sender,psd,receiver):
    smtp=smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(sender,psd)
    smtp.sendmail(sender,[receiver],msg.as_string())
    smtp.quit()

make_dir()
make_excel()
make_eamil('逸云资源','18553358533@163.com','yue_sun@chinacache.com')
send_email('smtp.163.com','18553358533@163.com','qweASD123','yue_sun@chinacache.com')
