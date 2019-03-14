#while True:
try:
    num=int(input('请输入:'))
    result=8/num
    print(result)

except ValueError:
    print('请输入数字')
except ZeroDivisionError:
    print('分母不能是0')
except Exception as result:    #默认必须要加进去获取未知错误
    print('未知错误%s'%result)
else:
    print('尝试成功')
finally:
    print('无论成功与否都会执行')
