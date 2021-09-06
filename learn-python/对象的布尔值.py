# 测试对象的布尔值
print('-------以下对象的布尔值是False---------')
print(bool(False))
print(bool(0))
print(bool(None))  # None的布尔值是False
print(bool(''))  # 空字符串的布尔值是False
print(bool([]))  # 空列表的布尔值是False
print(bool(list()))  # 空列表的布尔值是False
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print('-----------其他对象的布尔值都是True-----------')
print(bool('helloworld'))
print(bool(18))
