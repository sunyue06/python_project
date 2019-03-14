import requests,json

data ={'Authorization':'CC95AC02F3D28EA2B848258BE87F88F8',
       'Date':'2018-12-11 11:39:00',
       'Content-Type':'json'}
response=requests.get('http://openapi.exclouds.com/contentService/QueryCacheIp?domain=www.csair.com&detail=Y',
                      headers=data)
jd=json.loads(response.text)
a=(jd['results'])

for i in a:
    print('%s\t%s\t%s'%(i['ip'],i['isp'],i['pro']))


