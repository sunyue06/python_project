n=int(input('请输入行数:'))
x=1
while x <= n:
    y=1
    while y<=x:
        print('*',end='')
        y+=1
    print('')
    x+=1
print('结束')
