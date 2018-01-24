# 九九乘法表
# while循环写九九乘法表
print ( " 九九乘法表： "  )
i = 1
while i <= 9:
  j = 1
  while j <= i:
    mult = i * j
    print ( " %d * %d = %d" %( j, i, mult ), end = " " )
    j = j + 1

  i = i + 1
  print ( " \r " )

# for循环写九九乘法表
print ( " 九九乘法表： " )
numLoop = 10
for i in range( 1, numLoop ):
  for j in range( 1, i + 1 ):
    mult = i * j
    print(" %d * %d = %d" % (j, i, mult), end=" ")

  print ( " \r " )

# 使用enumerate遍历
sequence = [ 12, 34, 34, 23, 45, 76, 89 ]
for i, j in enumerate( sequence ):
  print ( i, j )

# 上面代码等同于下面代码
sequence = [ 12, 34, 34, 23, 45, 76, 89 ]
for i in range( len( sequence ) ):  # 要熟练使用range()和len()的联合使用
  print ( i, sequence[i] )

# 求和
a = sum( range( 0,101 ) )
print ( " 0 - 100 之和为: ", a )

# pass的作用：pass只是为了防止语法错误
if a > 1:
  pass  # 如果没有内容，可以先写pass，但是如果不写pass，就会有语法错误

# python1：显示10次"happy"
i = 1
while i <= 10:
  print ( i, " happy! " )
  i = i + 1

# python2: 计算2+4+6+8+10
sum = 0
for i in range( 2, 11, 2 ):
  print ( " i = ", i )
  sum += i
print ( " 2 + 4 + 6 + 8 + 10 = ", sum )

# 用while循环写上面代码
i = 2
sum = 0
while i <= 10:
  sum = sum + i
  i = i + 2
print ( " 2 + 4 + 6 + 8 + 10 = ", sum )

# python3: 负数递增
for i in range( 10,0,-1 ):  # 从10输出到1
  print ( i )

# python4: 内层循环输出
for i in range( 1, 4 ):
  for j in range( 1, 4 ):
    print ( " i, j = ", i, j )

# python5: 猜体重
import math
eps = 0.1
real_weight = 53.11
print ( " 请输入猜测值： " )
guess_weight =  float(input())
while math.fabs( real_weight - guess_weight ) > eps:
  print(" 请重新输入猜测值: ")
  guess_weight = float(input())
else:
  print(" you are rigth! ")

# for循环与while循环中有else时，执行完else后面的代码，整个循环就结束
sites = [ "Baidu", "Google", "Runoob", "Taobao" ]
for site in sites:
  if site == "Runoob":
    print ( " luk " )
    break # 跳出整个循环
  print ( " 元素： ", site )
else:
  print ( " 没有循环元素 " )

print ( " 循环完毕！ " )

# python6: 测试continue，相当于fortran中的cycle
nfloor = 9
i = 0
while i <= 9:
  i = i + 1
  if i == 4:
    continue
  print(" i = ", i)

# 测试break，相当于Fortran中的exit
import math
eps = 0.1
real_weight = 53.11
a = 1
print ( " 请输入猜测值： " )
guess_weight =  float(input())
while a == 1:
  if math.fabs( real_weight - guess_weight ) > eps:
    print(" 请重新输入猜测值: ")
    guess_weight = float(input())
  else:
    print(" you are rigth! ")
    break