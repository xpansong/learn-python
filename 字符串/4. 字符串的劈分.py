'''使用split（）对字符串进行劈分，默认空格字符串是劈分符，劈分后是列表'''
s='hello python world'
lst=s.split()
print(lst)

'''split（）函数可通过sep和maxsplit进行限定，则使用sep指定特定字符串是劈分符,可以使用maxsplit指定劈分的最大次数'''
s1='hello|python|world'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

'''rsplit（）函数从右侧开始劈分'''
print('----------使用rsplit（）进行劈分--------------')
print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))