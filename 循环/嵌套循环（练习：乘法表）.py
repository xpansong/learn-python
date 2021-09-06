#打印九九乘法表

for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(i,'*',j,'=',i*j,end='\t')
    print()

for i in range(1,10):
    for j in range(1,1+i):
        print(i, '*', j, '=', i * j, end='\t')
    print()