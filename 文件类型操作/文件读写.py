file_read=open('23.txt.txt',)
file_write=open('23bak.txt','w')
while True:

    text=file_read.readline()
    if not text :
        break
    file_write.write(text)

file_read.close()
file_write.close()