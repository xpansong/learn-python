#从键盘录入密码，最多录入三次，如果正确就结束流程
for item in range(3):
    print("----")

#if结构
for item in range(3):
    key=int(input('请输入密码'))
    if key==123456:
        print('密码正确')
        break
    else:
        print('密码错误')

#while循环结构
key=int(input('请输入密码'))
t=0
while key!=123456:
    print('密码输入错误')
    t+=1
    key = int(input('请输入密码'))
    if t>=2:
        break
    if key==123456:
        break