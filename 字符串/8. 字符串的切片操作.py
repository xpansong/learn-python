s='hello,python'

s1=s[:5]   #不指定起始位置，从0开始
print(s1)

s2=s[6:]   #不指定结束位置，到最后结束
print(s2)

s3='!'
print(s1+s3+s2)

print('---------------切片标准格式[start:end:step]------------------')
print(s[1:5:1])  #从1开始，包括1，到5结束，不包括5，步长为1
print(s[::2])    #从0开始，到最后结束，步长为2
print(s[::-1])   
print(s[-6::])





