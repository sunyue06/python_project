def xian(a):
    if shu(a):
        print('-'*a)
    else:
        print('无法打印')

def shu(a):
    if not isinstance(a,(int,float)):
        return False
        
    else:
        return True
n=int(input('请输入长度:'))
xian(n)

