print('------------提取交集，使用intersection（）或符号&--------------')
s1={10,20,30,40}
s2={30,40,70,80,90}
print(s1.intersection(s2))
print(s1 & s2)    #&符号是交集的意思，跟intersection（）是等价的
print(s1)
print(s2)

print('------------并集操作，使用union（）或符号|--------------')
print(s1.union(s2))
print(s1 | s2)   #|符号是并集的意思，跟union（）是等价的
print(s1)
print(s2)

print('------------差集操作，使用difference（）或符号”-“--------------')
print(s1.difference(s2))
print(s1-s2)

print('------------对称差集操作，使用symmetric_difference（）或符号”^“--------------')
print(s1.symmetric_difference(s2))
print(s1^s2)
