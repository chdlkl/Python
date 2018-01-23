# python中的循环语句有for和while
# 1. while循环
# 格式为：
# while 判断条件:
#   语句
# 注意：冒号和缩进。这点与if语句一样
# python1: 计算1到100的总和
# python中的while语句相当于Fortran中的do循环
n = 100
sum1 = 0
counter = 1
while counter <= n:
  sum1 = sum1 + counter
  counter += 1

print ( " 1 到 %d 之和为：%d " %( n, sum1 ) )
print ( " ------------------------------ " )
# python2: while循环使用else语句
# python中的while...else语句相当于fortran中的do...if...else语句
count = 0
while count < 5:
  print ( count, " 小于 5 " )
  count = count + 1
else:
  print ( count, " 大于或等于 5 " )

# python3: 简单语句组
flag = 1
# while ( flag ): print ( " welcome! " )
# 此语句为无限循环，相当于fortran中的do end do结构语句
print ( " Good bye! " )

# python4: for语句
# for循环可以遍历任何序列的项目，如一个列表或一个字符串
# for循环的一般格式如下：
# for <variable> in <sequence>:
#   <statements>
# else:
#   <statements>
# 注意：冒号和缩进
languages = [ "c", "c++", "Perl", "fortran" ]
for x in languages:
  print ( x )

# python5: for语句中使用break,break跳出整个循环体
# 判断循环与if语句，看缩进即可
sites = [ "Baidu", "Google", "Runoob", "Taobao" ]
for site in sites:
  if site == "Runoob":
    print ( " luk " )
    break # 跳出整个循环
  print ( " 元素： ", site )
else:
  print ( " 没有循环元素 " )

print ( " 循环完毕！ " )

# python6: range()函数
# 如果需要遍历数字序列，可以使用内置range()函数,它可以生成数列
for i in range(5):  # 生成5个数，默认从0开始。相当于fortran中的do i = 0, 4
    print ( i )

# range()也可以指定区间, 还有步长（可以是负数）。注意指定区间时range(n1,n2)输出的数据为n1---n2-1
# 注意如果步长刚好“合适”，最后一个数不输出，如下：
for i in range( 5, 9, 2 ):
    print ( i )  # 输出为5，7。9不输出

# 结合range()和len()函数, 这个例子要牢记！！！
a = [ "Google", "Baidu", "Taobao" ]
for i in range( len(a) ):  # len(a) = 3, range(3) = [ 0, 1, 2 ]
    print ( i, a[i] )

# 还可以使用range()函数创建列表
# list(range(5))

#python7: break：相当于Fortran中的exit
# break 语句跳出for和while的循环体。如果从for和while循环中终止，任何对应的循环else块将不执行
for letter in 'Runoob':
    if letter == 'b':
        break
    print ( " 当前字母为： ", letter )

var = 10
while var > 0:
    print ( " 当前变量值为： ", var )
    var -= 1
    if var == 5:
        break
else:
    print ( " Good bye! " )

# python8: continue 相当于fortran中的cycle
# continue用来告诉python跳过当前循环块中的循环语句，然后执行下一轮循环
for letter in 'Runoob':
    if letter == 'o':
        continue
    print ( " 当前字母为： ", letter )

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print(" 当前变量值为： ", var)
else:
    print ( " Good bye! " )
# 循环语句中可以有else子句，它在穷尽列表（for循环）或条件变为false（while循环）
# 导致熏昏终止时被执行，但循环被break终止时不执行

# 查询质数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
