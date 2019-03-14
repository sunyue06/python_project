# 小明体重75公斤
# 小明每次跑步减肥0.5公斤
# 小明每次吃东西会增加1公斤
#
# 类：人
# 属性：体重姓名
# 动作:跑，吃，增加

class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return '我的名字是:%s.我的体重是:%.2f公斤' %(self.name,self.weight)
    def run(self):
        self.weight -= 0.5
        print('%s 爱跑步，体重是%s' %(self.name,self.weight))

    def eat(self):
        self.weight += 1
        print('%s 爱吃东西，吃一次增加1公斤，我的体重是%s'%(self.name,self.weight))


xiaoming=Person('小明',80)
xiaomei=Person('小美',45)
print(xiaoming)
print(xiaomei)
xiaoming.run()
xiaomei.run()
xiaoming.eat()
xiaomei.eat()
