i=int(input('请输入行数:'))
a=1
while a <= i:
    b=i-1
    while b >= a:#这一行是空格
        print(' ',end='')
        b-=1
    c=1
    while c <= a : #这一行是输入*
        print('* ', end='')
        c += 1
    print('')
    a+=1

