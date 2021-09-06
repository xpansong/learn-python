#以追加模式打开文件，如果文件不存在则创建，如果文件存在，在文件末尾追加内容，而且，每执行一次程序，文件就追加一次内容
file=open('japan.txt','a')
print(file.write('java'))
file.close()

file=open('china.txt','a')
print(file.write('java'))
file.close()
