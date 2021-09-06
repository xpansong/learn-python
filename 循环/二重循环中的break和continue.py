print('二重循环中break的使用')
for i in range (1,5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

print('二重循环中continue的使用')
for i in range (1,5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j)