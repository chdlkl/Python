# Fibonacci series:两个元素的总和确定下一个数
a, b = 0, 1
# 这是一个复合赋值：变量a和b同时得到新值0和1
# 最后一行再次使用了同样的方法
while b < 10:
  print('',b)
  a, b = b, a + b

# print中使用end关键字
# 关键字end可以用于将结果输出到同一行
# 或者在输出的末尾添加不同的字符
# 比如：print ( '', b, end = ',' )
a, b = 0, 1
while b < 1000:
  print ( '', b, end = '' )
  a, b = b, a + b

# 输出变量值
i = 256 * 256
print ( ' i的值为： ', i )

# 一行输出多个数
a = 10; b = 38; c = 98
print ( a, b, c, sep = ',' )  
# sep函数后面所跟的字符可以将输出结果分开
# 如果不写sep函数，则输出结果之间用空格分开
