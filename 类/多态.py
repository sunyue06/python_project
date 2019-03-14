class Dog(object):

    def __init__(self,name):
        self.name=name
    def game(self):
        print('%s奔跑着玩耍'%self.name)

class XiaoTiandog(Dog):

    def game(self):
        print('%s飞在天上玩耍'%self.name)

class Person(object):
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dogname):
        print('%s %s开心的玩耍'%(self.name,dogname.name))
        #让狗玩耍
        dogname.game()


#1.创建一只狗
wangcai=Dog('旺财')
wang=XiaoTiandog('丰田')
#2.创建一个人
xiaoming=Person('小明')
#3.人跟狗一起玩
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(wang)