# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 09:11:38 2018

@author: luk
"""

#------------------------------------------------------------------#
# 2.1.1 创建
import numpy as np
# 创建一维数组
a = np.array( [1,2,3,4] ) # 元素之间不能用空格隔开
b = np.array( (5,6,7,8) )
a = 2*a
print ( " 2*a: ", a )

# 创建二维数组
c = np.array( [ [1,2,3,4],[4,5,6,7],[6,7,8,9] ] )  
print ( " array a: ", a )
print ( " array b: ", b )
print ( " array c: ", c )
m = len(c)  # 获取二维数组的行与列
n = len(c[0,:])
print ( " row c: ", m )  # m = 3
print ( " col c: ", n )  # n = 4
input()  # 暂停语句

# 输出二维数组
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )  # 换行
input()
# type( a.shape ) 为元组
print ( " a shape: ", a.shape, type(a.shape) )  # (4,) <class 'tuple'>
print ( " b shape: ", b.shape )  # (4,)
print ( " c shape: ", c.shape )  # (3,4)

for i in range( m ):
      print ( c[i,:], end = ' ' )  # c[i,:]也可以写成c[i][:]
      print ( '\n' )  # 换行
input()

# 改变二维数组c的形状
c.shape = 4, 3
m = len(c)  # 获取二维数组的行与列
n = len(c[0])  # 或len(c[0][:])
print ( " row c: ", m )
print ( " col c: ", n )
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )

# 当某个维度的元素个数是-1时，将自动计算此维度的长度
# 由于数组c有12个元素，因此下面的程序将数组c的shape改成了(2,6)
c.shape = 2, -1
m = len(c)  # 获取二维数组的行与列
n = len(c[0])  # len(c[0][:])
print ( " row c: ", m )
print ( " col c: ", n )
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )
a.shape = -1 # 对于一维数组还是其原来的size
print ( a )

# 使用数组的reshape()方法，可以创建指定形状的数组，而原数组的形状保持不变
# 但是这种情况，a和d是共享数据存储空间，一个改变，另一个也改变
d = a.reshape((2,2)) # 由于数组形状的type为tuple，所以是(2,2),不是[2,2]
print ( " d :", d )
# d的size是2*2，shape是(2,2)
print ( " d.shape: ", d.shape )  #(2,2)
print ( " d.size: ", d.size )   # size: 4 = 2*2
input()

# 由于共享内存，所以d的shape改变，a的shape也改变
e = a
e.shape = 2, 2
print ( " shape a: ", a.shape )  # (2,2)
print ( " e :", e ) # [ [2,4], [6,8] ]
a[1] = 100  # 改变a的第一行后e的第一行也改变
print( e )  # [ [2,4], [100,100] ]
input()

# sizd的用法
from numpy import random  
matrix1 = random.random(size=(2,4))  
# 每维的大小  
print( matrix1.shape )

# 对应矩阵元素相乘
# 对于aray对象：
a = np.array( [[1,2],[3,4]] )
b = np.array( [[4,3],[2,1]] )
print ( " a*b: ", a*b )

# 按矩阵运算法则相乘: np.dot和np.matmul运算结果一样
print ( " np.dot(a,b): ", np.dot(a,b) )
print ( " np.matmul(a,b): ", np.matmul(a,b) )

# 对于matrix对象：
a = np.mat( [[1,2],[3,4]] )
b = np.mat( [[4,3],[2,1]] )
# 对于matrix对象，'*'表示原生的矩阵乘法规则
print ( " a*b: ", a*b )
# multiply表示数量积
print ( " np.multiply(a,b): ", np.multiply(a,b) )

# 矩阵的转置
print ( " before transpose b: ", b )
b = np.transpose(b)
print ( " after transpose b: ", b )

#------------------------------------------------------------------#
# 2.1.2 元素类型
# 通过dtype参数在创建数组时指定元素类型
# float是64位的双精度浮点类型
# complex是128位的双精度复数类型
ai32 = np.array( [1,2,3,4], dtype = np.int32 )  # int32前面要加np.
af = np.array( [1,2,3,4], dtype = float )
ac = np.array( [1,2,3,4], dtype = complex )
print ( ' ai32 type: ', ai32.dtype )  # 获取数组的元素类型, int32
print ( ' af type: ', af.dtype )  # float64
print ( ' ac type: ', ac.dtype )  # complex128

# 使用astype()方法可以对数组的元素类型进行转化
t1 = np.array( [1,2,3,4], dtype = np.float )
t2 = np.array( [1,2,3,4], dtype = np.complex )  # np.complex默认complex128
t3 = t1.astype( np.int32 )
t4 = t2.astype( np.complex64 )  # complex64时需要指定

#------------------------------------------------------------------#
# 2.1.3 自动生成数组
# 一维数组
# 1. arange()类似于内置函数range(), 指定开始值，终值和步长
a = np.arange( 0, 1, 0.1, dtype = float )
print ( 'a = ', a )  # [0.1, 0.2, ...,  0.9]
# 2. linspace()通过指定开始值，终值和元素个数创建等差数列一维数组
# 可以通过endpoint指定是否包含终值，默认值位True, 即包含终值
b = np.linspace( 0, 1, 10, dtype = np.float64 )
print ( 'b = ', b )
# 3. logspace()创建的数组是等比数列。默认的基数是10
a = np.logspace( 0, 2, 5 )
print ( 'a = ', a )
b = np.logspace( 0, 1, 12, base = 2.0, endpoint = False )
print ( 'b = ', b )
input()
# 上面的三个函数创建的都是一维数组

# 二维数组
# 1. zeros()将数组初始化为0
a = np.zeros( (2,2), np.int32 )
# 2. ones()将数组初始化为1
b = np.ones( (2,3), dtype = float )
# 3. empty()只分配数组使用的内存，不对数组进行初始化操作
c = np.empty( 4, np.int32 )
# 4. full()将数组初始化为指定值
c = np.full( (2,3), np.pi )
# 此外， zeros_like(), ones_like(), full_like(), empty_like等函数创建与参数数组的
# 形状和类型相同的数组，因此zeros_like(a)与zeros( a.shape, a.dtype )的效果相同
# 5. 通过fromfunction()创建数组
def func1(i):
      return i % 4 + 1
a = np.fromfunction( func1, (10,) )  # 数组大小为10，但是i的范围为0-9

def func2( i, j ):
      return ( i + 1 ) * ( j + 1 )
b = np.fromfunction( func2, (9,9) ) # 数组大小为(9,9)，但是i和j的范围是0-8

#------------------------------------------------------------------#
# 2.1.4 存取元素
a = np.arange(10)  
# 默认从0开始10个数。mp.arange(start,end,step),元素个数为(end-start)/step
print( 'a = ', a ) # [0,1,2,3,4,5,6,7,8,9]
print ( a[5] )  # 获取第六个元素:5
print ( a[3:5] ) # 获取第四个到第五个元素:[3,4]
print ( a[:5] )   # 获取前5个元素:[0 1 2 3 4]. 不包括第6个元素
print ( a[:-2] ) # 去掉后面两个数:[0 1 2 3 4 5 6 7]
print ( a[5:1:-2] )  # 取[5,4,3,2]中的[5,3]，这个重点记忆
print ( a[1:-1:2] ) # [1,...,8]隔两个取一个:[1 3 5 7]
print ( a[::-1] ) # 颠倒数组a输出:[9 8 7 6 5 4 3 2 1 0]
# 不同于列表，数组可以修改片段
a[2:4] = 100, 101
print ( a ) # [  0   1 100 101   4   5   6   7   8   9]
b = a[3:7] # 不能b = a[3,4,5,6,7], 可以b = a[[3,4,5,6,7]]
print ( b ) # [101   4   5   6]
b[2] = -10
print ( a )  # [  0   1 100 101   4 -10   6   7   8   9]
print ( id(a), id(b) )  # a, b有相同的id

b = [1,2,3,4]
print ( a )  # [  0   1 100 101   4 -10   6   7   8   9]
print ( id(a), id(b) )  # 此时a, b有不同的id。因为b赋值的不是某一个数组的片段

# **使用列表作为下标得到的数组不和原始数组共享内存
x = np.arange( 10, 1, -1 )  # 9个数，9 = (10 - 1) / 1. x = [10,.., 2]. 不包括1
a = x[ [3,3,1,8] ]
b = x[ [3,3,-3,8] ] # 下标可以是负数，倒数第三个
b[2] = 100 # 修改其值
print ( b )  # b = [ 7, 7, 100, 2 ]
print ( x )  # x = [10 9 8 7 6 5 4 3 2] # 数组x不变

# 整数序列下标也可以用来修改元素的值
x[[3,5,1]] = -1, -2, -3
print ( x ) # x = [ 10,-3,8,-1,6,-2,4,3,2 ]
# **当下标是一维数组时，结果和用列表作为下标的结果相同
x = np.arange( 10, 1, -1 ) # x = [10,9,8,7,6,5,4,3,2]
a = x[np.array([3,3,1,8])] 
print ( a ) # a = [7,7,9,2]
# 当数组是多维数组时，得到的也是多维数组
a = x[np.array( [[3,3,1,8],[3,3,-3,8]] )]
# 将x[np.array([3,3,1,8])]和x[np.array([3,3,-3,8])]的元素重组
print ( a )  # 数组a的shape为(2,4). a = [ [7,7,9,2], [7,7,4,2] ]
input()

# 布尔数组
x = np.arange(5,0,-1)
print ( x ) # x = [5,4,3,2,1]
a = x[np.array( [True,False,True,False,False] )]  
# 数组a的值为True对应的值，False对应的值舍去
print ( a ) # a = [5,3]
# 布尔列表
a = x[ [True,False,True,False,False] ]
# 布尔列表与布尔数组功能相同
print ( a ) # a = [5,3]

# 布尔数组下标修改元素
# 将True对应处的值进行修改
x[np.array([True,False,True,True,False])] = -1, -2, -3
print ( x )

# 布尔数组下标的应用
x = np.random.randint(0,10,6) # 产生长度为6的随机数组，0-9之间，左闭右开
print ( x )
a = x[ x > 5 ]  # x > 5会产生一个长度为6的布尔数组
print ( a )

#------------------------------------------------------------------#
# 2.1.5 多维数组
a = np.arange(0,60,10).reshape(-1,1) + np.arange(0,6)
print ( a[0,3:5] ) # 第0行的第4列与第5列
print ( a[4:,4:] ) # 第5行与第6行的第5列与第6列
input()
print ( a[:,2] ) # 第3列
print ( a[2::2,::2] )  
# 2::2表示从第3行到末行，隔一行取值。::2表示从第0列到末列，隔一列取值
input()
# **如果下标元组中只包含整数和切片，那么得到的数组和原始数组共享数据，即有相同的id。
b = a[0,3:5]
b[0] = -b[0]
print ( a[0,3:5] )  # 数组片段a被改变

# 多维数组的下标中，也可以用整数元组或列表、整数数组和布尔数组
# 当下标使用这些对象时，所获得的数据是原始数据的副本，因此修改结果数组不会改变原始数组
a = np.arange(0,60,10).reshape(-1,1) + np.arange(0,6)
print ( a[(0,1,2,3),(1,2,3,4)] )  
# a[0,1],a[1,2],a[2,3],a[3,4]得到的是一维数组
print ( '---------------------------' )
b = a[(0,1,2,3),(1,2,3,4)] # 数组b为4行
b[0] = -1
print ( a[(0,1,2,3),(1,2,3,4)] ) # 原数组没有被改变

print ( a[3:,(0,2,5)] )  # 等同于a[3:,[0,2,5]]
# 这里需要注意一下，带冒号的数组片段不需要写在圆括号或是方括号中，只要离散的片段才需要

mask = np.array( [1,0,1,0,0,1], dtype = np.bool )
print ( a[mask,2] )  # mask返回一个逻辑数组，逻辑数组用作a第0轴的下标
# 如果mask不是布尔数组，而是整形数组、列表或元组时，就按整数数组为下标的方式进行运算
mask1 = np.array( [1,0,1,0,0,1] )  # mask1不是逻辑数组
mask2 = [ True, False, True, False, False, True ]
print ( '---------------------------' )
print ( 'a[mask1,2]: ', a[mask1,2] )
print ( 'a[mask2,2]: ', a[mask2,2] )

# 当下标的长度小于数组的维数时，剩余的各轴对应的下标是':'
print ( a[[1,2],:] )
print ( a[[1,2]] )  # 两者等价。不过不建议这样写，严谨一点总没错

# 当所有轴都用形状相同的整型数组作为下标时，得到的数组和下标的数组相同
# 下面三种方式等价
x = np.array( [[0,1],[2,3]] )
y = np.array( [[-1,-2],[-3,-4]] )
print ( a[x,y] )  # y作为列，其中的-1表示最后一列，以此类推
print ( a[(0,1,2,3),(-1,-2,-3,-4)].reshape(2,2) )
print ( a[[0,1,2,3],[-1,-2,-3,-4]].reshape(2,2) )

