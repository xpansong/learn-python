'''居中对齐的操作方法'''
s='hello,python'
'''居中对齐'''
print(s.center(20,'#'))  #20代表字符串+填充之后的总宽度
'''左对齐'''
print(s.ljust(20,'#'))   #20代表字符串+填充之后的总宽度
print(s.ljust(10))       #长度小于字符串长度的，返回原字符串
'''右对齐'''
print(s.rjust(20,'#'))
print(s.rjust(20))
print(s.rjust(10))
'''右对齐，只能指定一个参数，用0填充'''
print(s.zfill(20))
print(s.zfill(10))
'''特殊情形，字符是负数的情况，在整数前面加0'''
print('-888'.zfill(8))