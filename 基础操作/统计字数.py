a=input('请输入字符串:')
res={}
for i in a :
    if i in res :
        res[i]+=1
    else:
        res[i]=1
print(res)

