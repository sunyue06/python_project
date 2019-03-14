def demo1():
    return int(input('请输入:'))
def demo2():
    return demo1()

try:
    print(demo2())
except Exception as result:
    print('未知错误:%s' %result)