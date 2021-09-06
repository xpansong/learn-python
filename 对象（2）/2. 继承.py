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

class Teacher(Person):
    def __init__(self,name,age,teach_of_year):
        super().__init__(name,age)
        self.teach_of_year=teach_of_year

stu=Student('宋晓盼',33,'1001')
teacher=Teacher('张三',35,'9')
stu.info()    #info是从Person类继承来的
teacher.info()