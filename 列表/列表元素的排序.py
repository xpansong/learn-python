print('--------使用列表对象sort（）进行排序，不生成新的列表，原列表直接运算，不需要重新赋值----------')

lst=[10,90,398,34,21,77,68]
print(lst,id(lst))

#调用列表对象sort（），对列表进行升序排序
lst.sort()
print(lst,id(lst))

#通过指定关键字参数，对列表进行降序排序
lst.sort(reverse=True)
print(lst,id(lst))

print('-------使用内置函数sorted（）进行排序，生成新的列表，因此新列表需要重新赋值----------')
lst=[10,90,398,34,21,77,68]
new_list=sorted(lst)  #生成新的列表，new_list是新的列表，ID跟原列表不一样
print(new_list)

#通过指定关键字参数，对列表进行降序排序
list2=sorted(lst,reverse=True)
print(list2)
