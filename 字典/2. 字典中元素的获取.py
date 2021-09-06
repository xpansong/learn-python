print('---------字典中元素的获取---------')
#使用[]获取，如果查找的键不存在，输出keyerror
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])
#print(scores['陈六'])  #输入的键不存在，会报错KeyError

#使用get()获取，如果查找的键不存在，会输出None
scores={'张三':100,'李四':98,'王五':45}
print(scores.get('张三'))
print(scores.get('陈六'))  #输入的键不存在，会返回None
print(scores.get('麻七',99))  #99是查找的键不存在时返回的默认值