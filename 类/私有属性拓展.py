class A:
    def __init__(self):
        self.num1=100
        self.__num2=10
    def __test(self):
        print( 'num1的值为%s num2的值为%s' %(self.num1,self.__num2))

    def test(self):
        print('父类的公有方法%s'%self.__num2)
        self.__test()
class B(A):
    def demo(self):
        print('子类的方法%s' %self.num1)
        self.test()
    pass

b=B()
print(b.num1)
b.test()


