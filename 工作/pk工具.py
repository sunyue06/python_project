import requests
import json
import xlwt
import xlrd
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

a=''
excel_name=''
msg=''
def make_excel(url_name):
    global a
    global excel_name
    key='Date'
    value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data ={'Authorization':'CC95AC02F3D28EA2B848258BE87F88F8',
           'Content-Type':'json'}
    data[key]=value
    response=requests.get('http://openapi.exclouds.com/contentService/QueryCacheIp?domain=%s&detail=Y'%url_name,
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
    print('逸云资源已导出，文件名为:%s'%excel_name)

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
        #smtp.set_debuglevel(1)  #显示发送过程
        smtp.connect(mail_host)
        smtp.login(sender,psd)
        smtp.sendmail(sender,to_addrs,msg.as_string())
        smtp.quit()
        print('发送成功')
    except Exception as result:
        print('发送失败，异常为%s'%result)

def local_net():
    file_name=input('请输入文件名:')
    workbook=xlrd.open_workbook('C:/Users/yue.sun/Desktop/自己/py/工作/%s'%file_name,'r')#打开excel表格
    sheet_name = workbook.sheet_names()[0]  # sheet名字
    sheet = workbook.sheet_by_name(sheet_name)
    #sheet=workbook.sheet_by_index(0)#sheet索引从0开始
    sheet=workbook.sheet_by_name(sheet_name)
    print(sheet.name,sheet.nrows,sheet.ncols)
    cols_provice=sheet.col_values(2)
    cols_city=sheet.col_values(3)
    cols_pro=sheet.col_values(4)
    aim_cols_provice=sheet.col_values(10)
    aim_cols_city=sheet.col_values(11)
    aim_cols_pro=sheet.col_values(12)
    num=0
    local=xlwt.Workbook(encoding='utf-8')
    worksheet1=local.add_sheet('非本省本网')
    try:
        for     provice,city,pro,aim_provice,aim_city,aim_pro in zip(cols_provice,cols_city,cols_pro,aim_cols_provice,aim_cols_city,aim_cols_pro):
            if provice==aim_provice and city==aim_city and pro==aim_pro:
                continue
            else:
                #print(provice,city,pro,aim_provice,aim_city,aim_pro)
                worksheet1.write(num, 0, label=pro)
                worksheet1.write(num, 1, label=provice)
                worksheet1.write(num, 2, label=city)
                worksheet1.write(num, 3, label=aim_pro)
                worksheet1.write(num, 4, label=aim_provice)
                worksheet1.write(num, 5, label=aim_city)
                num+=1
                local.save('非本省本网%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d'))
        print('表格已导出，请前往脚本执行路径下查看')
    except Exception as reult:
        print('导出失败,异常为%s'%reult)

def show_menu():
    print('-'*50)
    print('输入1获得逸云资源:')
    print('输入2将逸云资源发送至指定邮箱(注意执行完1后才可以执行2):')
    print('输入3获得非本省本网表格:')
    print('-'*50)

def choose_menu():
    show_menu()
    while True:
        cm=input('请选择操作:')
        if cm=='1':
            url_name=input('请输入需要查询的域名:')
            make_excel(url_name)
        if cm=='2':
            receive=input('请输入收件人:')
            send_eamil(receive)
        if cm=='3':
            local_net()



if __name__ == '__main__':
    choose_menu()
