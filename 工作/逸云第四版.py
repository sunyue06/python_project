import requests
import json
import xlwt
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

a=''
excel_name=''
msg=''
def make_excel():
    global a
    global excel_name
    key='Date'
    value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data ={'Authorization':'CC95AC02F3D28EA2B848258BE87F88F8',
           'Content-Type':'json'}
    data[key]=value
    response=requests.get('http://openapi.exclouds.com/contentService/QueryCacheIp?domain=*.9iwuli.com&detail=Y',
                          headers=data)
    jd=json.loads(response.text)
    a=(jd['results'])
    num = 0
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('逸云资源')
    for i in a:
        worksheet.write(num, 0, label=i['ip'])
        worksheet.write(num, 1, label=i['isp'])
        worksheet.write(num, 2, label=i['pro'])
        num+=1
        workbook.save('逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d'))
        excel_name ='逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d')

def send_eamil(receiver):
    global msg
    sender = '18553358533@163.com'
    psd = 'qweASD123'    #是授权密码不是邮箱登录密码
    mail_host='smtp.163.com'
    subject='逸云资源'
    to_addrs=receiver.split(',')
    #创建带附件的实例
    msg=MIMEMultipart()
    msg['Subject']=Header(subject,'utf-8')
    msg['from']=Header(sender,'utf-8')
    msg['To']=",".join(to_addrs)      #多个收件人
    #创建正文，把文本添加到msg类中
    msg.attach(MIMEText('逸云节点资源，请查看附件','plain','utf-8'))
    #构造附件
    file_path='C:/Users/yue.sun/Desktop/自己/py/工作/%s'%excel_name
    att1=MIMEText(open(file_path,'rb').read(),
                  'base64','utf-8')
    #att1["Content-Type"]='application/octet-stream;name=%s'%Header(filename,'utf-8').encode('utf-8')         #与下边功能一致
    #att1["Content-Disposition"]='attachment;file_name=%s'%Header('%s'%filename,'utf-8').encode('utf-8')      #与下边功能一致
    att1.add_header('Content-Disposition', 'attachment', filename=excel_name)#没有这三行会出现文件结尾变成bin现象
    att1.add_header('Content-ID', '<0>')
    att1.add_header('X-Attachment-Id', '0')
    msg.attach(att1)#将附件添加到类文件
    try:
        smtp=smtplib.SMTP()
        smtp.set_debuglevel(1)  #显示发送过程
        smtp.connect(mail_host)
        smtp.login(sender,psd)
        smtp.sendmail(sender,to_addrs,msg.as_string())
        smtp.quit()
        print('发送成功')
    except Exception as result:
        print('发送失败，异常为%s'%result)

if __name__ == '__main__':
    make_excel()
    send_eamil('835448967@qq.com,yue_sun@chinacache.com')
