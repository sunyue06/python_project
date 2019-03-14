line = int(input('输入行数:'))

i = 1
while line+1>=i:
    print((' '*line) + ('*'*(i*2)))
    i += 1
    line -= 1
