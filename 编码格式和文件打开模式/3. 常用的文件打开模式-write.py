#以只写方式打开文件，如果文件不存在则创建，如果文件存在，则用新的内容覆盖原来的内容
file=open('usa.txt','w')   #如果这个文件原来没有，则创建一个文件
print(file.write('python'))   #文件的内容是python
file.close()    #读取的结果放到一个列表中

file=open('china.txt','w')   #如果这个文件原来有
print(file.write('中国'))   #则用新的python内容替换原来的内容
file.close()    #读取的结果放到一个列表中