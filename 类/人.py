class People:
    def __init__(self,name,height,age):
        print('初始化已完成')
        self.name=name
        self.height=height
        self.age=age
        print("我的年龄是%s" % self.age)
    # def people_info(self):
    #     print('我的姓名是:%s,我的身高是:%s,我的年龄是:%s'%(self.sex,self.color,self.high,self.weigh))
    def run(self):
        if self.name=='xiaoming':
            print('每天早上跑步')
        elif self.name=='xiaomei':
            print('不喜欢跑步')
    def eat(self):
        if self.name == 'xiaoming':
            print('会吃东西')
        elif self.name == 'xiaomei':
            print('喜欢吃东西')
    def __str__(self):
        return '我的姓名是:%s,我的身高是:%s'%(self.name,self.height)



n1=People('xiaoming','1.75','18')
print(n1,)
n1.run()
n1.eat()

