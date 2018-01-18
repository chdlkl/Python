# 字典可存储任意类型的对象
# 字典的每个键值（key=>value）对用冒号（:）分割
# 每个对之间用逗号（,）分割，整个字典写在花括号（{}）中
# d = { key1 : value1, key2 : value2 }
# python中的字典有点类似fortran中的type数据类型

# 字典中的键必须是唯一的，但值则不必
# 值可以取任意类型

dict1 = { 'abc': 456 }
print ( " dict1 is: ", dict1 )
dict2 = { 'abc': 123, 98.6: 37 }
print ( ' dict2 is: ', dict2 )
print ( ' dict2[98.6] is ', dict2[98.6] )

# 访问字典里的值
dict1 = { 'Name': 'lkl', 'Age': 24, 'Class': 1 }
print ( " dict1['Name'] is ", dict1['Name'] )
print ( " dict1['Age'] is ", dict1['Age'] )

# 修改字典
dict1['Age'] = 25   # 更新Age的值
print ( " dict1['Age'] is ", dict1['Age'] )
dict1['School'] = "Chang'An University"  # 向dict1里面添加信息
print ( " dict1['School'] is ", dict1['School'] )

# 删除字典及其元素
del dict1['Name']
print ( " after del the dict1['Name'] is ", dict1 )  # 删除字典中的底朝天['Name']
dict1.clear()  # 清空字典
del dict1  # 删除整个字典

# 字典键的特性
# 创建时如果同一个键出现两次，则后一个值被保留
dict1 = { 'Name': 'luk', 'Age': 4, 'Name': 'lkl' }
print ( " dict1 is ", dict1 )
print ( " dict1['Name'] ", dict1['Name'] )

# 字典中的键可以是数字，字符串，元组，不能是列表
dict1 = { 76: 12, 'Name': 'luk', ( 1, 2, 3 ): 1 }

print ( ' dict1 is ', dict1 )
print ( ' dcit1[76] is ', dict1[76] )
print ( ' dict1[(1,2,3)] is ', dict1[(1,2,3)] )
print ( " dict1['Name'] is ",dict1['Name'] )

print ( ' len(dict1) is ', len(dict1) )  # 计算字典元素个数
print ( ' str(dict1) is ', str(dict1) )  # 将字典输出成字符串
print ( ' type(dict1) is ', type(dict1) )  # 返回输入变量的类型
