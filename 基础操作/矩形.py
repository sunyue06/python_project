x=int(input('请输入矩形的长:'))
y=int(input('请输入矩形的宽:'))
a=1
b=1
while a <= x:
    b=1
    while b<=y:
        print('*',end='')
        b+=1
    print('')
    a+=1
print('打印完成')




