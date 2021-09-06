print('-------------类属性----------------')
class Student:
    native_place='吉林'
#print(Student.native_place)
#song=Student
#print(song.native_place)
#Student.native_place='天津'
#print(song.native_place)

#print('----------类方法----------')
    @classmethod
    def cm(cls):
        print('我是类方法')
Student.cm()

'''类属性、类方法和静态方法都是通过类名打点（Student.）去调用的，
实例方法是通过对象名（song.）打点或者类名打点去引用对象名(Student.cm(song))去调用的'''
