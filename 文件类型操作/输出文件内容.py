import  os
file_hello=[]
def find_hello_dir(father_dir,file_dir):
    file_path=os.path.join(father_dir,file_dir)
    if  os.path.isdir(file_path):
        for f in os.listdir(file_path):
            find_hello_dir(file_path,f)
    else:
        if  file_path.endswith('.py'):
            if find_hello_file(file_path):
                file_hello.append(file_path)

def find_hello_file(py_file):
    flag = False
    dakai = open(py_file,'rb')
    while True:
        line = dakai.readline()
        if line == '':
            break
        elif 'hehe' in line:
            flag = True
            break
    dakai.close()
    return flag
find_hello_dir('C:/Users/','yue.sun/')
print(file_hello)