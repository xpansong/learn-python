scores={'张三':100,'李四':98,'王五':45}

print('-------获取字典中的所有keys----------')
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))   #将所有keys组成的视图转换成列表

print('-------获取字典中的所有values----------')
values=scores.values()
print(values)
print(type(values))
print(list(values))

print('-------获取字典中的所有键值对----------')
items=scores.items()
print(items)
print(list(items))