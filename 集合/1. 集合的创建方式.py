#使用花括号,
s={5,7,8,34,6,7,5}  #集合中的元素是无序的
print(s)           #集合是和字典相同的底层数据结构，元素不允许重复，重复的元素删掉

#使用set()内置函数创建
s=set(range(6))    #将序列转化成集合
print(s)
print(type(s))

s=set(['python','world','love',99])  #将列表转换成集合
print(s)
print(type(s))

s=set((1,2,3,4,4,4,5))   #将元组转换成集合
print(s)
print(type(s))

s=set('python')  #将字符串序列转换成集合
print(s)

s=set({'python','love','you',87})  #将集合类型转换成集合类型
print(s)

print('-----------定义一个空集合------------')
'''s={}
print(s,type(s))'''  #花括号不能定义空集合，已经被字典类型占用了

s=set()       #空集合只能通过set（）内置函数来定义
print(s,type(s))