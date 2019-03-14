i = int(input('输入行数:'))
a = 0
while a < i:
    b = 0
    while b < a-1:#这一行是打印空格
        print(' ', end='')
        b += 1

    c = i - a
    while c > 0:#这一行是打印星号
        print('* ', end='')
        c -= 1
    print('')
    a += 1


