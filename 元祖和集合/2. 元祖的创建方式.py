#使用小括号创建元祖
t=('python','hello',30)
print(t,type(t))

#其中小括号可以省略
t2='python','hello',30
print(t2)
print(type(t2))

#如果只有一个元素，则必须加小括号和逗号,否则不是元组，是元素本身的类型
t3=('python',)
print(t3)

#使用tuple()内置函数
t=tuple(('python','hello',30))
print(t,type(t))

#创建空元组
lst=[]
print(lst)
lst=list()
print(lst)
d={}
print(d)
d=dict()
print(d)
t=()
print(t)
t=tuple()
print(t)