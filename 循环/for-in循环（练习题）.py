#找到100到999之间的水仙花数，153=3*3*3+5*5*5+1*1*1

for item in range(100,1000):
    a=item//100
    b=item%100//10
    c=item%10
    if item==(c**3+b**3+a**3):
        print(item)

