#字典生成式{item:price for item,price in zip(items,prices)}

print('--------两个列表元素数量一致----------')
items=['fruits','books','others']
prices=[96,78,85]
d={item:price for item,price in zip(items,prices)} #item后面加.upper()就会变成大写
print(d)

print('--------如果两个列表元素数量不一致，以少的元素为基准----------')
items=['fruits','books','others']
prices=[96,78,85,128,79]
dict={item:price for item,price in zip(items,prices)}
print(dict)