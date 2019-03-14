class Animal:

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def sleep(self):
        print('睡')

    def run(self):
        print('跑')

class Dog(Animal):
    def bark(self):
        print('汪汪')

class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞')
    def bark(self):
        print('吼吼')

xiaotianquan=XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.bark()


