file = open('23.txt.txt','a')

file.write('hello\n')
text=file.read()
print(text)


file.close()