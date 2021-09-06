#remove()函数一次只移除一个元素，如果存在重复，只移除第一个元素
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
lst.remove(30)
print(lst)

#pop（）函数，根据索引去移除对象
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
lst.pop(2)
print(lst)
#pop（）函数，不写索引，会将最后一个元素删除
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
lst.pop()
print(lst)

#使用切片一次至少删除一个元素，但切片会产生新的列表对象
print('-----------------')
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
lst2=lst[2:4]
print(lst2)
#如何不产生新的列表？反切
lst[2:4]=[]
print(lst)

#使用clear（）函数清除列表中的所有元素，括号中什么都不加
print('-----------------')
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
lst.clear()
print(lst)

#使用del去删除列表
print('-----------------')
lst=[10, 20, 30, 'love', 'hello', 'python', 30]
del lst
print(lst)