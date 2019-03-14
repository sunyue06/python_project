a=int(input('请输入数字:'))
x=1
while x<=a :
    y=1
    while y<=x:
        print('%s*%s=%s\t\t'%(y,x,y*x),end='')
        y+=1
    print('')
    x+=1
print('结束')



