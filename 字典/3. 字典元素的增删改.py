scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('Marry' not in scores)

del scores['李四']  #删除指定的键值对
print(scores)

#scores.clear()    #删除字典中的所有键值对
#print(scores)

scores['王二麻子']=98   #新增元素
print(scores)

scores['王二麻子']=100  #修改元素
print(scores)