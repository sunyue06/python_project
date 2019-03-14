import dns.resolver
import os
import http.client

iplist=[]
appdomain='www.baidu.com'

def get_iplist(domain=""):
    try:
        #dns.resolver.query()
        A=dns.resolver.query(domain,'A')
    except Exception as result:
        print('dns resolver error %s'%result)
        return
    for i in A.response.answer:

        for j in i.items:
            if j.rdtype==1:
                iplist.append(j.address)
            else:
                pass
    return True

def check(ip):
    checkurl=ip+':80'
    getcontent=''
    http.client.socket.setdefaulttimeout(5)
    conn=http.client.HTTPConnection(checkurl)

    try:
        conn.request('GET','/',headers={'HOST':appdomain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent=='<!doctype html>':
            print(ip+'OK')
        else:
            print(ip+'ERROR')

if __name__=="__main__":
    if get_iplist(appdomain)and len(iplist)>0:
        for ip in iplist:
            check(ip)
    else:
        print("1")