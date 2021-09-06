class Student:    #规范：类的名称可以使用一个或多个单词，每个单词的首字母大写，其余小写，Student是类对象
    native_place='吉林'  #类属性，在类之内、方法之外，整个类都可以调用
    #初始化方法
    def __init__(self,name,age):
        self.myname=name  #实例属性
        self.myage=age
    #实例方法
    def info(self):
        print('我的名字叫：',self.myname,'年龄是：',self.myage)
    #静态方法
    @staticmethod
    def method():
        print('我喜欢踢足球')
    #类方法
    @classmethod
    def cm(cls):
        print('我喜欢看电视')

song=Student('宋晓盼',33)   #创建Student类的对象，即实例对象
song.info()
Student.info(song)  #跟song.info()效果是一样的，两种调用方法
print(song.myname)
