a=20
b=100
c=a+b
print(c)
print('-------------实际执行的过程--------------')
c=a.__add__(b)
print(c)

print('----------------add()方法示例演示-----------------')
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name*2)

stu1=Student('张三')
stu2=Student('李四')
print(stu1+stu2)

print('------------------len()方法实例演示-------------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
#print(stu1.__len__())  程序报错，'Student' object has no attribute '__len__'
print(stu1.__len__())