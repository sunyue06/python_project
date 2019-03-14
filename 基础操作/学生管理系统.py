def show_menu():#打印选择参数
    print('-'*50)
    print('学生管理系统'.center(40))
    print('输入1，表示添加学生')
    print('输入2，表示查找学生')
    print('输入3，表示修改学生')
    print('输入4，表示删除学生')
    print('输入5，表示查看所有学生')
    print('输入6，表示退出管理系统')

def add_student():#添加学生
    name = input('学生的姓名是:')
    age = int(input('学生的年龄是:'))
    qq = int(input('学生的QQ号码是:'))

    stu['name'] = name
    stu['age'] = age
    stu['qq'] = qq
    students.append(stu)
    print('该生已添加完毕!')

def find_student(name):#查找学生

    for item in students:
        if item['name'] == name.strip():
            print('%s在本校' %name)
            show_all(item)
            break
    else:
        print('该%s不在学校' % name)

def change_student():#修改学生
    xgold = input('请输入需要修改的名字:')
    xgnew = input('请输入修改后的名字:')
    for item in students:
        if item['name'] == xgold.strip():
            item['name'] = xgnew
            print('%s已修改为%s' % (xgold, xgnew))
            break
    else:
        print('%s不在本校无法修改' % xgold)

def shanchu_student(name):#删除学生

    for item in students:
        if item['name'] == name.strip():
            students.remove(item)
            print('%s同学已删除' % name)
            break
    else:
        print('%s不在本校无法删除' % name)

def show_all(item):
    print('%s\t%s\t%s'%(item['name'], item['age'], item['qq']))

def show_all_studnets():#展示学生列表
    if stu in students:
        print('序号\t姓名\t年龄\tQQ号')
        for i, item in enumerate(students, 1):
            print('%s\t' %i,end='')
            show_all(item)

    else:
        print('学生列表未创建,请先创建列表然后在查询')


def main():#运行主程序
    show_menu()
    while True:
        cz = input('请选择操作:')
        if cz == '1':
            add_student()
        if cz == '2':
            name = input('请输入需要查找的姓名:')
            find_student(name)
        if cz == '3':
            change_student()
        if cz == '4':
            name = input('请输入需要删除的姓名:')
            shanchu_student(name)
        if cz == '5':
            show_all_studnets()
        if cz == '6':
            break
filename=open('students.txt','aw')
students=[]#全局变量
stu = {}
main()
filename.close()
