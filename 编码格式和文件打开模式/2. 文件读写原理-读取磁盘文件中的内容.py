#以只读模式打开文件
file=open('usa.txt','r')
print(file.readlines())
file.close()
