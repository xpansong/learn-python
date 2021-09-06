def calc(a,b):
    c=a+b
    return c

print('---------位置赋值-----------')
result1=calc(10,20)
print(result1)

print('-----------关键字赋值-------------')
result2=calc(a=20,b=10)   #等号左边的a和b是关键字参数
print(result2)