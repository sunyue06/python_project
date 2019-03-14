import os    #导入os
file_list=[]    #定义一个全局变量输出的文件名会添加在这个列表里
def find_hello(parent_dir,file_dir):   #定义一个函数参数是文件的父目录跟目录
    file_abspath=os.path.join(parent_dir,file_dir)    #利用os.path.join将两个路径合起来形成绝对路径
    if os.path.isdir(file_abspath):#判断传入的是不是目录
        for f in os.listdir(file_abspath):  #列举绝对路径下的文件
            find_hello(file_abspath,f)  #递归调用函数
    else:
        if file_abspath.endswith('.py'):#判断文件是不是以.py结尾
            if  read_hello(file_abspath):    #调用12行函数
                file_list.append(file_abspath)    #将满足条件的文件添加进开头定义的列表中
def read_hello(py_file):   #定义一个函数，参数是文件名字
    flag = False    #立一个标志
    f = open(py_file)   #打开文件
    while True:      #死循环
        line = f.readline()     #读文件，因为line每次只会显示一行，所以需要来一个循环来一直输出内容，从而进行对比
        if line == '':    #结束条件，如果line读完了就是''
            break      #退出
        elif c in line:    #如果的文件包括想要查找的内容
            flag = True     #标志就会重新指向True
            break   #退出
    f.close()   #关闭文件
    return flag     #返回flag的值，整个函数会输出True（执行第11行）或者False


a=input('请输入父目录:')
b=input('请输入子目录:')
c=input('请输入想要查找的内容:')
find_hello(a,b)
print(file_list)