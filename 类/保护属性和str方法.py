flag=False
f=open(a.txt)
while True:
    line =f.readline()
    if line == '':
        break
    elif 'ip' in line:
        flag=True
        print(line)
        break
f.close()
