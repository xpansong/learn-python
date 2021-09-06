print('----------------使用new创建对象------------------')
class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))
'''创建实例对象'''
p1=Person('张三',20)   #等号是赋值的意思，会先执行等号右侧的代码

print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))

'''总结1：传参的过程
先执行等号右边的代码Person('张三',20)，Person通过__new__方法传给cls，所以cls类和Person类的id相同；
继续执行方法，创建了对象obj，生成新的id；
返回obj，传给self，所以self的id和obj的id相同，此时对象创建完成——初始化完毕；
把self传给p1
'''
'''总结2：__new__方法在前用于创建对象，__init__方法在后是为这个对象的实例属性进行赋值，最后将创建的对象放到p1之中进行赋值'''

