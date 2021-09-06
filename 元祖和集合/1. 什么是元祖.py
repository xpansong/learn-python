#不可变序列：字符串、元组，不能执行增删改的操作，如果执行，则对象地址改变
print('---------不可变序列：字符串--------')
s='hello'
print(s,id(s))
s=s+'world'
print(s,id(s))

#可变序列：字典、列表，进行增删改操作，对象地址不发生更改
print('---------可变序列：列表--------')
lst=['python','hello',90]
print(lst,id(lst))
lst[0]=100
print(lst,id(lst))

print('---------元组的定义---------')
t=('python','world',98)
print(t)