s='hello,hello'
print(s.index('lo'))  #3
print(s.rindex('lo')) #9
print(s.find('lo'))   #3
print(s.rfind('lo'))  #9

'''使用index（）查找不存在的字符，抛异常；使用find（）查找不存在的字符，抛出-1'''
#print(s.index('k'))  #ValueError: substring not found
print(s.find('k'))
#print(s.rindex('k'))  #ValueError: substring not found
print(s.rfind('k'))