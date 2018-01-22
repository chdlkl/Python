# -*- coding:utf-8 -*-
# 1. python1
height = float( input( " please input the heigth: " ) ) 
weight = float( input( " please input the weight: " ) )
# 输入数据时，一定要加int，float等，不然type是字符串
if weight > height - 100.0:
  print ( " too fat! " )
else:
  print ( " under control! " )

# 2. python2
rain = float ( input( " please input the rain: " ) )
wind = float ( input( " please input the wind: " ) )
if rain >= 500 or wind >= 10:  # 此处逻辑判断与fortran不同，fortran是.or.
  print ( " class is over! " )
else:
  print ( " as usual! " )

# 3. python3
source = float( input( " please input the source: " ) )
if source >= 90 and source <= 100:
  print ( " Grade = A " )
elif source >= 80:
  print ( " Grade = B " )
elif source >= 70:
  print ( " Grade = C " )
elif source >= 60:
  print ( " Grade = D " )
elif source >= 0:
  print ( " Grade = E " )
else:
  print ( " Grade = ? " )

# 4. python4
print ( " please input x, y: " )
x, y = map( float, input( '' ).split() ) # 这一行代码用来读取多个数据，左边是一个变量时，存在列表里 
print ( ' x, y is ', x, y )
if x > 0:
  if y > 0: # x > 0 and y > 0
    ans = 1
  elif y < 0: # x > 0 and y < 0
    ans = 4
  else:  # x > 0 and y = 0
    ans = 0
elif x < 0:
  if y > 0: # x < 0 and y > 0
    ans = 2
  elif y < 0: # x < 0 and y < 0
    ans = 4
  else:  # x < 0 and y = 0
    ans = 0
else:  # x = 0
  ans = 0

if ans != 0:
  print ( ' %d quadrant! ' %( ans ) )
else:
  print ( ' on the axis! ' )

# 5. python5
import math
eps = 1e-15
b = 3.0
a = math.sqrt(b) ** 2 - b
if math.fabs( a - 0.0 ) < eps:
  print ( ' a == 0.0 ' )
else:
  print ( ' a != 0.0 ' )
print ( ' a =  ', a )

# 6. python6
str1 = input( " please input str1: " )
str2 = input( " please input str2: " )
if str1 > str2:
  relation = '>'
elif str1 == str2:
  relation = '='
else:
  relation = '<'

print ( " %s %s %s " %( str1, relation, str2 ) )

# 总结
# 1. 读取多个数据时，语句为x,y[z,...] = map( int, input().split() )，其中的int也可以换为float等
# 2. input读取数据，无论输入什么类型的数据，都是字符串
# 3. 如果想转换，则为a = int( input() )
# 4. 使用数学函数，必须先import math
