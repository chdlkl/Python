# 访问字符串中的值
var1 = 'hello world!'
var2 = 'luk'
print ( 'var1[0]: ', var1[0] ) 
# 这里要注意
# 1. python中的元素下标从0开始，Fortran中默认从1开始
# 2. 引用方式也不一样，python是[]，fortran是()
# 3. 引用单个元素时，比如，python是var[1]，fortran是var(1:1)

# 字符串更新（替换）
var = 'lkl'
print ( 'before var:', var )
var = var[0] + 'uk'
print ( 'after var', var )

# 字符串运算符
a = 'hello'; b = 'python'
print ( ' a is ', a )
print ( ' b is ', b )
print ( ' a + b is ', a + b ) # 字符串拼接，fortran用//拼接字符串
print ( ' a*2 is ', a * 2 ) # 连续输出字符串a两次

if ( 'h' in a ):  # 判断字符'h'是否在字符串a中
    print ( ' h in a ' )
else:
    print ( ' h not in a ' )

# 字符串格式化
print ( ' I am %s, and I am %d years old! ' %( 'luk', 10 ) ) # 这里单引号中的内容与%后面内容之间无逗号

# 数字格式化
print ( '%.15f' %(1.2) ) # 格式化输出数字，python为%.15f输出15位小数，fortran为fn.15，此处的n一般要满足n-15>=3

# 按规律输出字符
a = 'abcdefgh'
print ( a[::2] ) # 从第一个字符输出，步长为2

# 使用负数从字符串右边末尾向左边反向索引，最右侧索引为-1，正向的话，最左侧为0
str = 'luklukluk'
print ( str[-3] )
