source_file='C:/Users/yue.sun/Desktop/自己/py/基础操作/test1.txt'
mudi_file='copy'+source_file[source_file.rfind('/')+1:]
print('移动后文件名为:')

yuan=open(source_file)
mudi=open(mudi_file,'w')

wenjian=yuan.read()
mudi.write(wenjian)

yuan.close()
mudi.close()

