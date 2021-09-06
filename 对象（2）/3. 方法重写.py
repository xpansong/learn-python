print('----------方法重写---------------')
'''如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写'''
'''子类重写后的方法中可以通过super().XXX()调用父类中被重写的方法'''
class Person:   #也可以写Person（object）
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):        #方法重写
        super().info()     #调用父类中的方法
        print(stu.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teach_of_year):
        super().__init__(name,age)
        self.teach_of_year=teach_of_year
    def info(self):
        super().info()
        print(teacher.teach_of_year)

stu=Student('宋晓盼',33,'1001')
teacher=Teacher('张三',35,'9')
stu.info()    #info是从Person类继承name和age，从子类继承stu_no
teacher.info()