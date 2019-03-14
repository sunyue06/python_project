class Person:
    #初始化对象方法，不是构建对象方法
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight


    def print_info(self):
        print('姓名:%s,年龄:%s,身高%s,体重:%s'%(self.name,self.age,self.height,self.weight))

p=Person('sunyue',24,183,70)
p.print_info()