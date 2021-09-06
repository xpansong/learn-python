print('--------------斐波拉契数列，每一项等于前两项之和------------------')
#设置一个变量n，fac(n)
def fac(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fac(n-1)+fac(n-2)
print(fac(6))

print('------------输出数列前6位的数字-----------------')
for i in range(1,7):
    print(fac(i),end='\t')
