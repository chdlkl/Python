s = 'hello, luk!'
print ( str(s) ) # 用str()函数输出的字符串不带''，用repr()函数输出的字符串带''
print ( repr(s) ) # 用str()函数和repr()函数输出数字都不带''

x = 10 * 3.25
y = 200 * 200
s = 'x value is: ' + str(x) + ', y value is: ' + repr(y)
print ( s )

# repr()函数可以转义字符串中的特殊字符
hello = 'hello, luk\n'
print ( str(hello) ) # str()函数会将\r认为是换行符，repr()函数可以原样输出
print ( repr(hello) )

# 输出平方与立方表
for x in range( 1, 11 ):
  # rjust()：将字符串靠右，并在左边填充空格
  # ljust()和center()类似
  print ( repr(x).rjust(2), repr(x*x).rjust(3), end = ' ' )
  print ( repr(x*x*x).rjust(4) )

# 另一个方法是zfill()，它会在数字的左边填充0
s = '12'.zfill(5) # 用5个位宽输出，左边三位是0
print (s)
s = '-3.14'.zfill(7) # 负号(-)与小数点(.)也占位宽
print (s)
s = '3.141592653'.zfill(5)  # 超过位宽，原样输出 
print (s)

# str.format()的基本使用
print ( '{} {}!' .format( 'https://', 'www.baidu.com' ) ) 
# 大括号{}会被format()中的参数替换掉，里面的字符会照样输出

# 在括号中的数字用于指向传入对象在format中的位置
print ( ' {0} and {1} ' .format( 'Google', 'baidu' ) )
print ( ' {1} and {0} ' .format( 'Google', 'baidu' ) )

# 如果在format()中使用了关键字参数，那么他们的值会指向使用该名字的参数
print ( ' {name}: {site} ' .format( name = 'baidu', site = 'www.baidu.com' ) ) 

# 位置及关键字参数可以任意组合, 0, 1, other与输出参数对应，后面的数字为输出的位宽
print ( ' {0:10}, {1:10} and {other:10}. ' .format('Google','baidu',other = 'taobao') )

for x in range(1,11):
  print ( '{0:2d} {1:3d} {2:4d}' .format(x, x*x, x**3) )


import math
print ( " pi: {0:.3f} " .format( math.pi) ) # 0对应的是pi，.3f是格式化输出

table = { 'Google': 1, 'baidu': 2, 'Taobao': 3 }
for name, number in table.items():
  print ( '{0:6} ==> {1:4d}' .format(name,number) )

# 读和写文件
# open ( filename, mode )
# filename: 是一个包含了要访问的文件名称的字符串值
# mode: 决定打开文件的模式：只读，写入，追加等。
# mode 为 r 时，只读；r+ 读写。 指针都在文件开头
# mode 为 w 时，写入；w+ 读写，如果该文件已存在则将其覆盖，如果不存在， 创建该文件
# mode 为 a 时，打开一个文件用于追加。如果该文件存在，文件指针放在文件末尾，新的内容会被写在已有内容之后。如果没有文件，创建新文件写入
# mode 为 a+ 时，打开一个文件用于读写。如果该文件已存在，文件指针会放在文件的结尾。如果该文件不存在，创建新文件用于读写

f = open( 'foo.txt', 'w' )
f.write( "python is a good language!\nbut fortra more better!" )
f.close()

# 检测f.readline()
# f.readline()会从文件中读取单独一行。换行符为'\n'。f.readline()如果返回一个空字符串，说明已经读取到最后一行
f = open( 'foo.txt', 'r' )
i = 0
while True:
  str1 = f.readline()
  if str1 == '':
    break
  print ( str1 )
  i = i + 1
f.close()
print ( i )

# 检测f.read()
# 为了读取一个文件的内容，调用f.read(size)：读取一定数目的内容返回
# size是一个可选的数字类型参数。当size省略或者为负数时，读取文件所有内容
f = open( 'foo.txt', 'r' )
str1 = f.read(1) # 读取第一个字符
print ( str1 )
str1 = f.read() # 读取剩下的字符
print ( str1 )

# 检测f.readlines()
# f.readlines()将返回该文件中所包含的所有行
# 如果设置参数sizehint,则读取指定长度的字节，并且将这些字节按行分割
f = open( "foo.txt", 'r' )
str1 = f.readlines()
print ( str1 )
f.close()

f = open( "foo.txt", 'r' )
str1 = f.readlines(1) # 读取第一行
print ( str1 )
f.close()

# 读取每行
f = open( "foo.txt", 'r' )
for line in f:
  print ( line, end = '' ) # 加上end = ''，输出行之间无空行
f.close()

# f.write()：f.write(string)将string写入到文件中，可以返回写入的字符数
f = open( "foo.txt", 'a' )
f.write( '\n' )
num = f.write( '123' ) # 只能写入字符串
print ( num )
f.close()

# 如果写入的不是字符串，需要先进行转换
f = open( "foo1.txt", 'w' )
value = ['123', 14]
for i in value:
  print (i)
  s = str(i)
  f.write( s ) # 默认不换行
  f.write( '\n' )
f.close()
