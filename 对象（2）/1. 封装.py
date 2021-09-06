print('----------面向对象的三大特征-----------')
'''封装'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age   #age不希望在类的外部使用，所以加了__
    def show(self):
        print(self.name,self.__age)
song=Student('宋晓盼',33)
song.show()
print(song.name)
#print(song.__age)  #在类之外不能使用，不想让其他人在类之外访问，那么就绝对不能访问吗？
print(dir(song))
print(song._Student__age)  #自己挖坑自己埋，能否访问全凭自觉
