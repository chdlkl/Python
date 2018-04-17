import numpy as np
x = np.linspace( 0, 2*np.pi, 10 )
y = np.sin( x )  # ufunc函数产生的结果为数组
z = np.sin( x, out = x )  # 使用out将计算的结果存储在x数组中

# -------------------------------------------------------------------------------
# 比较运算和布尔运算
a = np.array( [1, 2, 3] )
b = np.array( [3, 2, 1] )
print( a < b )  # [ True, False, Flase ]
print( a != b )  # [ True, False, True ]

a = np.arange( 5 )
b = np.arange( 4, -1, -1 )
print( a == b )  # [False False True False False]
print( a >= b )  # [False False True  True  True]
print( np.logical_or( a==b, a>b ) )  # 等效于print ( a >= b )

# 对两个布尔数组使用and\or\not等进行布尔运算时，需要使用all()或any()
# and等只能作用于单个的逻辑元素，不能作用于逻辑数组整体
print( np.any( a == b ) )  
# a == b 返回[False False True False False]，里面有True元素，所以输出为True
print( np.any( a > b ) )  # a > b 返回[False False False True True]，输出为True
print( np.any( a == b ) and np.any( a > b ) )  # 根据上面，输出True

# 位运算
# 1. 与运算&
# a == b返回[False False True False False]，a > b返回[False False False True True]
print( (a==b)&(a>b) )  # 所以&运算返回[False False False False False]
print(  np.bitwise_and((a==b),(a>b)) )  # 与上句等效
# 2. 或运算|
# a == b返回[False False True False False]，a > b返回[False False False True True]
print( (a==b)|(a>b) )  # 所以|运算返回[False False True True True]
print(  np.bitwise_or((a==b),(a>b)) )  # 与上句等效
# 3. 非运算~
# a > b返回[False False False True True]
print( ~(a>b) )  # 所以~运算返回[True True True False False]
print(  np.bitwise_not((a>b)) )  # 与上句等效
# 4. 异或运算^(异或：相同为假，不同为真)
# a == b返回[False False True False False]，a > b返回[False False False True True]
print( (a==b)^(a>b) )  # 所以^运算返回[False False True True True]
print(  np.bitwise_xor((a==b),(a>b)) )  # 与上句等效

# -------------------------------------------------------------------------------
# 动态数组
# 1. 一维
import numpy as np
from array import array
a = array( 'd', [1,2,3,4] ) # 创建一个array数组
# 通过np.frombuffer() 创建一个和a共享内存的Numpy数组
na = np.frombuffer( a, dtype = np.float )
print( a ) # array('d', [1.0, 2.0, 3.0, 4.0])
print( na ) # [ 1.  2.  3.  4.]
na[1] = 20
print( a ) # array('d', [1.0, 20.0, 3.0, 4.0])
print( na ) # [  1.  20.   3.   4.]

# 2. 二维
import math
# =============================================================================
# while ( j < 3 ):  # 与下句j的for循环等价
#       j = j + 1
#       print( j )
# =============================================================================
for j in range(3):
      buf = array( 'd' )  
      # 要是将动态数组的定义写在j的循环之外，在j循环内清空动态数组的内存回报错
      for i in range(5):
            buf.append( math.sin(i*j*0.1) )
            buf.append( math.cos(i*j*0.1) )
      data = np.frombuffer( buf, dtype = np.float )
      data = data.reshape( -1, 2 )
      print( data )
      # del buf 与下句等价
      buf = []
      print( '--------------------------------' )