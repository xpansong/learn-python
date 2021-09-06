print('-----------创建一个类----------------')
class Student:     #规范：Student是类的名称（类名），由一个或多个单词组成，每个单次的首字母大写，其余小写
    pass
'''python一切皆对象，那么Student是对象吗？如果是，应该由三部分组成，ID+type+value'''
print(id(Student))   #有内存空间，开辟内存地址了
print(type(Student)) #class类型
print(Student)       #<class '__main__.Student'> value值

class People:
    eyes = 2     #直接写在类里的属性，成为类属性

    def __init__(self, height, weight):
        self.myheight = height
        self.myweight = weight

    def grow(self, n):   #在类之内定义的称为方法，在类之外定义的称为函数
        self.myweight+=n
song=People(160, 110)
zhang=People(178, 130)

print('--------------------')
print('我的体重是:',song.myweight, song.myheight, song.eyes)
print(zhang.myweight, zhang.myheight, zhang.eyes)
song.grow(5)
print(song.myweight, song.myheight, song.eyes)
print(zhang.myweight, zhang.myheight, zhang.eyes)
print('--------------------')

def people(height,weight,eyes):
    print(height,weight,eyes)


people(160,110,2)

print('-------------------------------')
'''给十个数，每个数都是半径，计算每个圆的面积'''
'''def calc(a):
    square=3.14*(a**2)
    return square
lst=[12,3,5,3,6,4]
for i in lst:
    print(calc(i))'''
print('-------------------------------')
class Circle:
    def __init__(self,r):
        self.r=r
    def calc(self):
        square=3.14*(self.r**2)
        return square
c1=Circle(4)
print(c1.calc())
