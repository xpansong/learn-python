file=open('japan.txt','a')
#print(file.write('hello'))
lst=['python','java','go']   #定义一个列表，通过writelines（）追加内容，字符串不留空格不换行
print(file.writelines(lst))
file.close()