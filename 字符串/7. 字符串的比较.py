print('-------字符串的比较---------')
'''比较规则：首先比较字符串中的第一个字符，如果相等继续比较下一个字符，直到两个字符不相等，
其比较结果就是字符串的比较结果，后面字符就不再被比较'''
print('apple'>'app')     #True
print('apple'>'banana')  #False

print('---------比较的是什么？原始值-------------')
'''字符串的比较，比较的是什么？比较原始值，可使用ord（）函数调到字符的原始值'''
print(ord('a'),ord('b'))
print(ord('宋'))

print('----------通过原始值查询字符-------------')
'''可使用内置函数chr得到指定原始值所对应的字符'''
print(chr(97),chr(98))
print(chr(23435))

print('---------字符串的判断-----------')
'''==与is进行比较的区别：
   ==比较value是否相等，
   is比较ID是否相等'''
a=b='python'
c='python'
print(a==b)
print(a==c)
print(a is b)
print(a is c)

