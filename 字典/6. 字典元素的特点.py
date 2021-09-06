#字典中的key不允许重复，value可以重复
print('-------key不允许重复，否则第二个key会覆盖第一个key--------')
scores={'张三':100,'张三':90}  #如果key重复，第二个键值对会把第一个键值对覆盖掉
print(scores)

print('-------value可以重复---------')
scores={'张三':100,'李四':100}
print(scores)

