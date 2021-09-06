#从键盘录入两个整数，然后判断数值的大小
num1 = input('请录入第一个整数')
num2 = input('请录入第二个整数')
print(num1, '大于', num2) if num1 > num2 else print(num1, '小于等于', num2)
#问题：视频中num用整数函数int进行转换，输出用str函数进行转换且使用连接符+，是否有必要？