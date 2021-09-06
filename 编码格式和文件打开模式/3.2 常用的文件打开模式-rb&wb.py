#如何打开二进制文件
src_file=open('desk.png','rb')
target_file=open('copydesk.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()