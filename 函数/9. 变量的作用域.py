print('------------局部变量-----------------')
def fun(a,b):
    c=a+b
    print(c)
#print(c)     #程序报错，c是局部变量，只在函数内部有效，在函数外部不发生作用
#print(a)

print('-----------全局变量-------------')
name='宋晓盼'  #name的作用范围为函数的内部和外部，称为全局变量
print(name)
def fun():
    print(name)
fun()

def fun():
    global name
    name='张三'
    print(name)
fun()
print(name)




