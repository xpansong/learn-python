print('--------------特殊方法和特殊属性------------------')
class A(object):
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name):
        self.name=name
class D(A):
    pass

x=C('张三')
print('------------------获得对象绑定的所有属性和方法------------------------')
print(x.__dir__())   #有特定参数，返回对象的所有有效的属性名
print(dir(x))
print(C.__dir__)     #没有参数，返回局部作用域中的名称列表
print('------------------获得类和对象绑定的所有属性和方法的字典------------------')
print(x.__dict__)
print(C.__dict__)

print(C.__bases__)
print(C.__base__)
print(x.__class__)
print('-----------------------------')
print(dir(x))
print('-----------------------------')
class XXXXX:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return 2*(self.x + other.x)

a=XXXXX(10)
b=XXXXX(10)
print(a+b)


