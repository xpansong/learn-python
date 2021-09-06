def fun(a,b):
    print(a)
    print(b)
    a=100
    b.append(10)
    print(a)
    print(b)

c=13
d=[22,33,44]
print(c)
print(d)
fun(c,d)   #位置传参，a、b是函数定义处的形参，c、d是函数调用处的实参，形参名称和实参名称可以不一样
print(c)
print(d)

'''在函数调用过程中，进行参数的传递，
   如果实参是不可变对象，在函数体内的修改不会影响实参的值，a的修改不会影响c的值；
   如果实参是可变对象，在函数体内的修改会影响实参的值，b的修改会影响d的值'''