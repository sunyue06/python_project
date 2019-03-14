def mi(none):
a=input('please input a number:')
n=int(a)
list1=range(1,n+1)
sum = 0
for x in list1:
    n = n-1
    sum = sum + x ** x
print (sum)


