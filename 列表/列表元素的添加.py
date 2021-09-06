#向列表末尾添加一个元素,列表的ID不变
lst=[10,20,30]
print(lst,id(lst))
lst.append(50)
print(lst,id(lst))

#向列表末尾添加多个元素
lst = [10, 20, 30]
'''for item in range(1,101):
    lst.append(item)
print(lst)'''

lst2=['hello','python',23]
'''append是在列表最后添加一个元素，因此lst2被识别为一个元素
lst. append(lst2)
print(lst)'''

#extend是最列表最后添加多个元素，因此lst2里的元素都被拆分
lst.extend(lst2)
print(lst)

#insert是在特定位置插入一个元素，语法结构insert(索引，添加对象）
lst.insert(3,'love')
print(lst)

#切片，即整体替换
lst[1:]=lst2  #是指将索引1之后的元素全部删除，替换为lst2
print(lst)

