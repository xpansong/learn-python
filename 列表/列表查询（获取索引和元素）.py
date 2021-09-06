'''获取特定元素的索引，使用函数index()'''
lst=['hello','world',98,'hello']
print(lst.index('hello'))  #有多个相同元素，只获取相同元素中第一个元素的索引
#print(lst.index('python')) #如果查询的元素不存在，则会报错ValueError: 'python' is not in list
print(lst.index('hello',1,4))  #可以在指定的start和stop之间查找特定元素

'''获取特定索引所对应的元素，格式lst[]'''
lst=['hello','world',98,'hello','world',234]
#获取索引为2的元素
print(lst[2])
#获取索引为-3的元素
print(lst[-3])
#获取索引为10的元素
#print(lst[10])   #如索引不存在/超范围，IndexError: list index out of range