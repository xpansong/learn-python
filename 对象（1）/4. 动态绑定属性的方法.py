class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'吃了苹果，','他今年'+str(self.age)+'了')
song=Student('宋晓盼',33)
zhang=Student('张杰',34)    #一个Student类可以创建N多个Student类的实例对象，每个实例对象的属性值不同
print(song.name)
song.eat()        #一定要牢记，这是方法，调用方式跟函数不一样！！！！！！！！！！！！！
zhang.eat()
print('------------动态绑定属性-----------------')
#给宋晓盼同学添加一个gender
song.gender='女'
print(song.name,song.age,song.gender)
print(zhang.name,zhang.age)
print('------------动态绑定方法-------------')
def show():      #这是一个函数，但绑定到对象上之后就成为方法了
    print('我在操作动态绑定方法')
zhang.show=show  #通过动态绑定，把函数变成方法
zhang.show()     #方法的调用模式
#song.show()     'Student' object has no attribute 'show'，因为song并没有绑定show方法