print('---------------给变量进行赋值-----------------')
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)

print('---------------浅拷贝----------------')
'''python对象如有没有特殊说明，都是浅拷贝'''
disk=Disk()     #创建一个硬盘类的对象
computer=Computer(cpu1,disk)    #创建一个计算机类的对象
#开始浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
'''浅拷贝，对象包含的子对象内容不拷贝，而只是引用'''


