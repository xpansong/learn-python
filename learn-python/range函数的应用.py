#第一种创建方式，range（stop）
r = range(10)   #默认从0开始，包含本数，到10结束（不包括），步长为1
print(r)        #返回值是一个迭代器对象，不会输出具体参数
print(list(r))  #用于查看range对象中的整数序列    -->list是列表的意思

#第二种创建方式，range(start, stop)
r = range(1, 10)  #默认从1开始，包含本数，到10结束，不包含本数，步长为1
print(list(r))

#第三种创建方式，range（start, stop, step)
r = range(1, 10, 2)   #默认从1开始，包含本数，到10结束，不包含本数，步长为2
print(list(r))

#判断指定的整数在数列中是否存在，in或者not in
print(3 in r)
print(10 in r)
print(11 not in r)