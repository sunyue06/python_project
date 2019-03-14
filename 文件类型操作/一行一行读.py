file=open('23.txt.txt')
while True:
    text=file.readline()
    if not text:
        break
    print(text,end='')
file.close()