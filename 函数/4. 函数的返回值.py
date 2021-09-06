def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
'''函数的调用'''
lst=[23,55,35,56,78,23,74,90]
print(fun(lst))

'''函数的返回值：
   1. 如果函数没有返回值，即函数执行完毕之后，不需要给调用处提供数据，return可以省略不写；
   2. 如果函数只有1个返回值，直接返回类型；
   3. 如果函数有多个返回值，返回的是元组'''

print('---------第1种情况------------')
def fun1():
    print('hello')
fun1()
print('-----------第2种情况，返回原值--------------')
def fun2():
    return 'hello'
print(fun2())
print('---------第3种情况,返回元组---------')
def fun3():
    return 'hello','world'
print(fun3())

'''函数在定义时，是否需要返回值，视情况而定'''