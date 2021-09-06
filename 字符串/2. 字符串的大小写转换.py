'''字符串大小写转换操作，字符串是不可变序列，转换后生成新的字符串对象'''
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))

'''转换后即便字符串没变，仍然全是小写，也会生成新的字符串对象'''
print(s.lower(),id(s.lower()))
print(s,id(s))

'''使用swapcase（）函数进行大小写转换'''
s1='Hello,Python'
print(s1.swapcase())

'''使用title（）函数把每个单词的首字母变成大写'''
print(s1.title())

'''使用capitalize（）函数把第一个字符的首字母变成大写'''
print(s1.capitalize())
