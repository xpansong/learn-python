s={10,20,30,40,66,22,23,56,67}
'''集合元素的判断操作'''
print(20 in s)
print(54 not in s)

'''集合元素的添加操作'''
s.add(88)   #add（）一次添加一个元素
print(s)

s.update({200,400,300})   #一次至少添加一个元素
print(s)
s.update(('python',45,86))
print(s)
s.update(['python',45,86])
print(s)

'''集合元素的删除操作'''
s={10,20,30,40,66,22,23,56,67}

print('---------使用remove（）方法，删除指定元素----------')
s.remove(67)
print(s)
'''s.remove(500)   #元素不存在则抛KeyError
print(s)'''

print('---------使用discard（）方法，删除指定元素----------')
s.discard(500)   #元素不存在也不抛异常，会把原来的集合抛出来
print(s)

print('---------使用pop（）方法，删除任一元素，不能指定元素----------')
s.pop()
print(s)

print('---------使用clear()方法，清除集合----------')
s.clear()
print(s)