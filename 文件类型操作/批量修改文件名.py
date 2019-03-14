import os

source_file=os.listdir('C:/Users/yue.sun/Desktop/自己/py/ceshi/')
print('文件包括:%s'%source_file)
for i in source_file:
    dest_file='re'+i
    father_dir=os.path.abspath('ceshi')
    print(father_dir)
    source=os.path.join(father_dir,i)
    dest=os.path.join(father_dir,dest_file)
    os.rename(source,dest)
    print('文件名从%s已修改为%s'%(source,dest))




