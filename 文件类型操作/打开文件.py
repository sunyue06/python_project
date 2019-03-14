#源文件路径及复制路径
source_file='C:/Users/yue.sun/Desktop/自己/py/基础操作/test1.txt'
aim_file='copy'+source_file[source_file.rfind('/')+1:]
print('目标文件名字%s'%aim_file)

#打开源文件
yuan=open('C:/Users/yue.sun/Desktop/自己/py/基础操作/test1.txt')
md=open(aim_file,'w')

#读源文件
content=yuan.read()
md.write(content)
#关闭文件
yuan.close()
md.close()