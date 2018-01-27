# 1. 迭代器
# 迭代器是一个可以记住遍历位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束。迭代器只向前
# 迭代器有两个基本方法：iter()和next()
# 字符串，列表或元组对象都可以用于创建迭代器
list = [1, 2, 3, 4]
it = iter( list ) # 创建迭代器
for x in it:
  print ( x, end = " " )
print ( "\r" )

# 使用next函数
import sys
list = [1, 2, 3, 4]
it = iter( list ) # 创建迭代器
while True:
  try:
    print ( next(it), end = " " )
  except StopIteration:
    sys.exit()
print ( "\r" )
