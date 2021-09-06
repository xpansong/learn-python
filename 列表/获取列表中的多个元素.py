#列表切片的标准格式：[start:stop:step]，需要特别注意包括start但不包括stop

lst=[10,20,30,40,50,60,70,80]
print('------step为正数的情况------')
#获取start为1，stop为6，步长是1的元素
print(lst[1:6])  #多种写法相等，例如[1:6:1]=[1:6:]=[1:6]
#源列表和新列表的ID值并不相同
print('原列表：',id(lst))
lst2=lst[1:6]
print('第二个列表：',id(lst2))
#获取start为1，stop为6，步长是2的元素
print(lst[1:6:2])
#如果start省略，默认从列表最头上开始切片
print(lst[:6:2])
#如果stop省略，默认切片到列表最后一个元素
print(lst[1::2])

#如果step为负数
print('-------step为负数的情况-------')
#默认从最后一个元素切片到第一个元素结束
print(lst[::-1])
#start=7，stop省略，step=-1，表示从第7个元素从后往前切片到第一个元素结束
print(lst[7::-1])
#start=6，stop=0，step=-2，表示从第6个元素从后往前切片到第二个元素结束，步长为2
print(lst[6:0:-2])
