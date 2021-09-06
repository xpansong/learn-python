class Student:    #没有写父类，默认继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字叫{0}，今年{1}岁了。'.format(self.name,self.age)

stu=Student('张三',20)
'''使用dir函数查看stu实例对象的所有属性和方法'''
print(dir(stu))
'''使用dir函数查看Student类对象的所有属性和方法，这些属性和方法并不是Student类自己定义的，而是从父类object类继承的，而Student类可以使用'''
print(dir(Student))
print('--------------object类里有个str方法，用于对象的描述------------------')
print(stu)   #默认执行stu.__str__()
'''也可以重写__str__方法，用于重写属性值'''