#计算从0到100的和
a=0
b=0
while a<100:
    a += 1
    b += a
print(b)

#计算1到100之间的偶数和
#四部判断法
sum=0
#初始化变量
a=2
#条件判断
while a<101:
    sum+=a
    a+=2
    print(sum)

#计算1到100之间的偶数的和
#四步判断法
sum=0
#初始化变量
a=1
#条件判断
while b<=100:
    #条件执行体（求和）
    b=a+1
    sum+=(b)
    #改变变量
    a+=2
print(sum)

sum=0
a=1
while a<=100:
    if a%2==0:
        sum+=a
    a+=1
print(sum)

