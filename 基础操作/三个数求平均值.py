def avg_3num(a,b,c):
    if shu_3num(a) and shu_3num(b) and shu_3num(c):
        return (a+b+c)/3
    else:
        print('无法计算平均数')
def shu_3num(a):
    if not isinstance(a,(int,float)):
        print('输入的数字%s不是数字'%a)
        return False
    else:
        return True

#a=int(input('请输入数字1:'))
#b=int(input('请输入数字2:'))
#c=int(input('请输入数字3:'))
s=avg_3num(4,'fge','wer')
print(s)