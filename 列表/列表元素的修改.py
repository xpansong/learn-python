#为指定索引赋予一个新值
lst=[10, 20, 'love', 'hello', 'python', 30]
lst[3]=60     #替换单个元素不需要加[]
print(lst)

#为指定切片赋予一个新值
lst=[10, 20, 'love', 'hello', 'python', 30]
lst[1:5]=[500,600,700]   #注意赋予的新值需要加[]
print(lst)
lst[2:4]='hi'
print(lst)          #问题：为什么这里会把h和i给拆开？

