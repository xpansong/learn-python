import package1.module_A
print(package1.module_A.add(11,22))
print('------------给被导入的模块起个别名---------------')
import package1.module_A as example
print(example.add(33,44))

print('------------注意事项---------------')
'''使用import导入时，只能跟包名或者模块名'''
import package1
import package1.module_A
import module_cited
'''使用from……import……导入时，可以导入包名、模块名、函数、变量等'''
from package1 import module_A
from package1.module_A import add

