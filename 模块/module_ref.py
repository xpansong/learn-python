print('--------------导入module_cited模块中的add方法------------------')
import module_cited
print(module_cited.add(10,20))

from module_cited import add
print(add(11,22))