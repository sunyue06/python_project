n=int(input('请输入行数:'))
x=n
while x>=1:
    y=1
    while y<=x:
        print('*',end="")
        y+=1
    print('')
    x-=1
print('结束')


