print('----------------读取文件的方法---------------------')
file=open('china.txt','r')
#print(file.read())  #read()会把文件中的所有内容读取出来，可以在括号中加数字，设置读取的字符个数
#print(file.readline())  #readline()会把文件中第一行内容读取出来
print(file.readlines())  #readlines()会把文件中每一行作为独立的字符串，放到列表中返回



