def test(a,b,func):
    result=func(a,b)
    return result

x=int(input('请输入数字:'))
y=int(input('请输入数字:'))
func_new=input('请输入想要的操作:')
func_new=eval(func_new)#eval 把字符串转换为python可执行的表达式
print (test(x,y,func_new))