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
        #1.针对子类特有的需求编写代码
        #2.使用super（）。调用原本在父类中封装的方法
        #3.增加其他子类的代码
        print('吼吼')
        super().bark()
        print('#$%&^$*&*%$#')

xiaotianquan=XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.bark()