# 访问列表中的元素
list1 = [ 'Google', 'Runoob', 'luk', 1993, 2000 ]
list2 = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
print ( ' list1[0]: ', list1[0] )
print ( ' list2[1:5]: ', list2[1:5] ) # 列表输出后，数据仍有[]，而字符串没有''或""

# 改变列表
list1 = [ 'Google', 'luk', 1993, 1994 ]
print ( ' The third element is : ', list1[2] )
list1[2] = 2008  # 此处一定要注意，列表中的元素可以改变，字符串中的单个元素不能用赋值的方法改变
print ( ' after update the third element: ', list1[2] )
print ( ' after update the list is: ', list1 )

# 删除列表中的元素
# 可以使用del语句来删除列表中的元素
list1 = list1
print ( ' before del the third element: ', list1 )
del list1[2]
print ( ' after del the third element: ', list1 )

# 列表脚本操作符
list1 = [ 1, 2, 3 ]
print ( ' the length of list1 = [ 1, 2, 3 ] is: ', len(list1) )
list2 = [ 4, 5, 6 ]
print ( ' [1,2,3] + [4,5,6] = ', list1 + list2 )
list1 = [ 'hi' ]
print ( ' list1 is: ', list1 )
print ( ' list1*4 is: ', list1*4 )

if ( 3 in [ 1,2,3 ] ):
  print ( ' 3 in [1,2,3] ' )
else:
  print ( ' 3 not in [1,2,3] ' )

# 列表截取与拼接
L = [ 'Google', 'luk', 'taobao' ]
print ( ' L[2] is: ', L[2] )
print ( ' L[-1] is: ', L[-1] ) # -1表示最左边第一个
print ( ' L[1:] is: ', L[1:] )

# 嵌套列表
a = [ 'a', 'b', 'c' ]
n = [ 1, 2, 3 ]
x = [ a, n ]
print ( ' x is: ', x )
print ( ' x[0] is: ', x[0] )
print ( ' x[0][1] is: ', x[0][1] )

# 创建一维列表
L = [ i for i in range(0,15) ]  # 相当于fortran中的 L = [ ( i, i = 1, 10 ) ]
print ( ' L is: ', L )
print ( ' L[::2] is: ', L[::2] ) # L[start:end:span]
# 创建二维列表
list_2d = [ [ 0 for col in range(5) ] for row in range(5) ]
list_2d[0].append(3); list_2d[0].append(5) # 替换第一行的数字，从最后一个数字填
list_2d[2].append(7)
print ( ' list_2d is: ', list_2d )

# 列表的复制
a = [ 1, 2, 3 ]
print ( ' origin a is: ', a )
b = a 
b[1] = 0
print ( ' change b[1] = 0, the a is: ', a )
print ( ' id(a) is: ', id(a), ' id(b) is: ', id(b) ) # 这样赋值，id相同，改变b中元素后，a中相应位置元素也会改变，这点很是蛋疼
a = [ 1, 2, 3 ]
print ( ' origin a is: ', a )
b = a[:]
b[1] = 0
print ( ' change b[1] = 0, the a is: ', a )
print ( ' id(a) is: ', id(a), ' id(b) is: ', id(b) )
# id不同，改变b中元素后，a中相应位置的元素不会改变。字符串无论是=还是[:]赋值，id均相同，没有list这种情况
