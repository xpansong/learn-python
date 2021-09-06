s='天涯共此时'
print('----------编码----------------')
print(s.encode(encoding='GBK'))  #在GBK这种编码格式中，一个汉字占两个字节
print(s.encode(encoding='UTF-8'))  #在UTF-8这种编码格式中，一个汉字占三个字节

print('----------解码----------------')
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
'''编码和解码的格式一定要相同'''
byte1=s.encode(encoding='UTF-8')
print(byte1.decode(encoding='UTF-8'))