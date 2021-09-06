#要求输出1到50之间的5的倍数
for i in range(1,51):
    if i%5==0:
        print(i)

for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)