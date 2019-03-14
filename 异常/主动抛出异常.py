def passwd_info():
    psd=input('请输入密码:')
    if len(psd)>=8:
        return psd
    err=Exception('输入密码不足八位')
    raise err
try:
    print(passwd_info())
except Exception as result:
    print('未知错误:%s'%result)