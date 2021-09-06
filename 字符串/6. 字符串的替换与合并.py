print('----------使用replace（）去替换掉字符串中的指定字符------------')
s='hello,Python'
print(s.replace('python','java'))  #需注意，区分大小写，字符大小写错了就不做替换操作
print(s.replace('Python','java'))

print('----------第三个参数是最大替换次数------------')
s1='hello,python,python,python'
print(s1.replace('python','java'))    #最后不指定参数，就全部替换
print(s1.replace('python','java',2))  #如果指定参数为2，那就只替换两次

print('----------使用join（）将列表和元组中的字符串合并成一个字符串------------')
lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))
t={'hello','python','java'}
print(''.join(t))

print('----------使用join（）将字符串合并------------')
print('*'.join('python'))