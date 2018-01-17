# python的元组tuple与列表类似，不过元组的元素不能修改
# 元组使用小括号()，列表使用方括号[]
# 元组的创建：只需要在括号中添加元素，并使用逗号隔开
tup1 = ( 'Google', 'luk', 1993, 1994 )
tup2 = ( 1, 2, 3, 4, 5 )
tup3 = ( 'a', 'b', 'c', 'd' )
print ( ' tup1[0] = ', tup1[0] )
print ( ' tup2[1:5] = ', tup2[1:5] )
print ( ' tup3 = ', tup3 )

# 创建空元组
tup1 = ()

# 元组中只包含一个元素时，需要在元素的后面添加逗号，否则括号会被当作运算符使用
tup1 = (50)
print ( ' tup1 = ', tup1 )
print ( ' type(tup1): ', type(tup1) ) # 不加逗号，类型为整型

tup1 = (50,)
print ( ' tup1 = ', tup1[:] )
print ( ' type(tup1): ', type(tup1) )  # 加逗号，类型为元组

# 修改元组
tup1 = ( 12, 34, 56 )
print ( ' tup1 = ', tup1 )
tup2 = ( 'abc', 'xyz' )
print ( ' tup2 = ', tup2 )
# tup1[0] = 100, 这种修改对元组来说非法，对字符串也非法，但是对列表可以
# 创建一个新元组
tup3 = tup1 + tup2
print ( ' tup1 + tup2 = ', tup3 )

# 删除元组，用del函数
del tup3

# 元组运算符
print ( ' len(tup1): ', len(tup1) )
print ( ' tup1*3: ', tup1*3 )
if ( 12 in tup1 ):
  print ( ' 12 in tup1 ' )
else:
  print ( ' 12 not in tup1 ' )

# 元组的索引与截取
L = ( 'Google', 'luk', 'Taobao' )
print ( ' L is ', L )
print ( ' L[2] is ', L[2] )
print ( ' L[-2] is ', L[-2] ) # -1表示最左边第一个
print ( ' L[1:] ', L[1:] )

# 元组内置函数
print ( ' len(L) is ', len(L) )
print ( ' max(L) is ', max(L) )
print ( ' min(L) is ', min(L) )

# 将列表转为元组用函数tuple
list1 = [ 'luk', 'fyn' ]
print ( ' list1 is ', list1 )
tup = tuple(list1)
print ( ' transpose list1 to tup is ', tup )

# 下面看一个"可变的"tuple
t = ( 'a', 'b', [ 'A', 'B' ] )
print ( ' t before is ', t )
t[2][0] = 'X'
t[2][1] = 'Y'
print ( ' t after is ', t )
