print('----------判断是否为合法标识符--------')
print('hello'.isidentifier())
print('123'.isidentifier())
print('张三'.isidentifier())
print('张三_123'.isidentifier())
print('-----------判断是否全部由空白字符组成（回车、空格、水平制表符）---------')
print('\t'.isspace())
print('-----------判断是否全部由字母组成------------')
print('abc'.isalpha())
print('张三'.isalpha())
print('张三1'.isalpha())
print('---------判断指定字符串是否为十进制数字---------')
print('123'.isdecimal())
print('11二'.isdecimal())
print('ⅡⅡ'.isdecimal())
print('---------判断指定字符串是否全部由数字组成----------')
print('123'.isnumeric())
print('123四'.isnumeric())
print('ⅡⅡⅡ'.isnumeric())
print('--------是否全部由字母和数字组成---------')
print('123adf'.isalnum())
print('张三123'.isalnum())