def get_num(n):
    if n<2:
        return 1
    return get_num(n-1)+get_num(n-2)

nums=[]
for i in range(20):
    nums.append(get_num(i))
print(nums)
