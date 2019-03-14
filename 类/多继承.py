class A:
    def test(self):
        print('A---test 方法')
    def demo(self):
        print('A---demo 方法')


class B:
    def demo(self):
        print('B---demo 方法')
    def test(self):
        print('B---test')
class C(B,A):
    pass

c=C()
c.demo()
c.test()
print(C.__mro__)
