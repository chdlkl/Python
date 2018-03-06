import numpy as np
# 创建一维数组
a = np.array( [1,2,3,4] )
b = np.array( (5,6,7,8) )

# 创建二维数组
c = np.array( [ [1,2,3,4],[4,5,6,7],[6,7,8,9] ] )  
print ( " array a: ", a )
print ( " array b: ", b )
print ( " array c: ", c )
m = len(c)  # 获取二维数组的行与列
n = len(c[0])
print ( " row c: ", m )
print ( " col c: ", n )

# 输出二维数组
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )  # 换行

# tyep( a.shape ) 为元组
print ( " a shape: ", a.shape, type(a.shape) )
print ( " b shape: ", b.shape )
print ( " c shape: ", c.shape )

# 改变二维数组c的形状
c.shape = 4, 3
m = len(c)  # 获取二维数组的行与列
n = len(c[0])
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
n = len(c[0])
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
print ( " d.shape: ", d.shape )
print ( " d.size: ", d.size )

# 由于共享内存，所以d的shape改变，a的shape也改变
e = a
e.shape = 2, 2
print ( " shape a: ", a.shape )
print ( " e :", e )
a[1] = 100
print( e )

# sizd的用法
import numpy as np  
from numpy import random  
matrix1 = random.random(size=(2,4))  
# 每维的大小  
print( matrix1.shape )