import itchat
import webbrowser
itchat.auto_login(hotReload=True)
user_name=itchat.search_friends('大哥')[0]['UserName']
itchat.send_file('C:/Users/yue.sun/Desktop/自己/py/工作/逸云资源2018-12-18.xls',toUserName=user_name)
print('发送成功')