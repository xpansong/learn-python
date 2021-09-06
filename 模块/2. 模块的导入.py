print('--------------使用import进行导入，导入的是模块之中的所有---------------')
import math
print(id(math))
print(type(math))
print(math)
print('-----------------------------------------------')
print(math.pi)
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))  #pow函数运算2的3次方，输出类型float
print(math.ceil(9.001),type(math.ceil(9.001)))  #ceil()函数找到比这个数大的最近的整数
print(math.floor(9.001))   #floor()函数找到比这个数小的最近的整数

print('--------------使用from 模块名称 import 函数/类/变量 进行导入，导入的是指定的内容---------------')
from math import ceil
print(ceil(9.99))