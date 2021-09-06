print('--------------sys模块：与python解释器及其环境操作相关的标准库----------------')
import sys
print(sys.getsizeof(20))
print(sys.getsizeof('李四'))
print('------------time模块，提供与时间相关的各种函数的标准库-----------------')
import time
print(time.time())
print(time.localtime(time.time()))
print('------------urllib包，读取来自网上服务器的数据标准库-----------------')
import urllib.request  #urllib是一个包，包里有一个request模块
print(urllib.request.urlopen('http://www.baidu.com').read())
print('------------math模块-----------------')
import math
print(math.pi)

