import requests,json,xlwt,datetime

key='Date'
value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data ={'Authorization':'CC95AC02F3D28EA2B848258BE87F88F8',
       'Content-Type':'json'}

data[key]=value

response=requests.get('http://openapi.exclouds.com/contentService/QueryCacheIp?domain=download3.sqntbw.com&detail=Y',
                      headers=data)
jd=json.loads(response.text)
a=(jd['results'])

num = 0
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('逸云资源')
filename=''
for i in a:

    worksheet.write(num, 0, label=i['ip'])
    worksheet.write(num, 1, label=i['isp'])
    worksheet.write(num, 2, label=i['pro'])
    num+=1
    workbook.save('逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d'))
    filename ='逸云资源%s.xls'%datetime.datetime.now().strftime('%Y-%m-%d')
print(filename)
