# 函数规则：
# 函数代码块以def关键词开头，后接函数标识符名称（函数名）和圆括号()
# 任何传入参数和自变量必须放在圆括号中间
# 函数内容以冒号起始，并且缩进
# return [表达式]结束函数。不代表达式的return相当于返回none
# python1
def hello():
  print ( " hello, world! " )

hello ( )  # 自定义函数用于输出信息

# python2
import math
def area( r ):
  s = math.pi * r * r
  return s

print ( " area = ", area(1.0) )

def print_luk( name ):
  return name
print ( " name = ", print_luk( "luk" ) )

# python3
# 定义函数
def printme( str1 ):
  return str1

# 调用函数
print ( printme( ' luk ' ) )
# 这里要注意，当用print调用函数时，函数中的所有语句都会执行。如果只写了return，后面没有表达式，会返回none
printme( " luk " )
# 如果直接写函数名，因为函数没有任何执行语句，就算有返回值，也无任何输出

# python传不可变对象
def ChangeInt(a):
  print ( ' before a = ', a )
  a = 10
  print ( ' after a = ', a )
  return a
b = 2
print ( " func value: ", ChangeInt(b) )
print ( " b = ", b )
# 经过测试，建议写print ( 函数名(参数) )，即print ( ChangeInt(b) )
# 如果写ChangeInt(b)不会输出信息

# python传入可变参数
def Changme( list1 ):
  list1.append( [1,2,3,4] )
  print ( " in : ", list1 )
  return list1

list2 = [ 10, 20, 30, 40 ]
Changme( list2 )  # 如果写成Change( list2[:] )，则两者的id不同
print ( " out : ", list2 )

# 特别注意
def Changeme( mylist ):
  mylist = [1,2,3,4];
  print ( " In function: ", mylist )
  return
mylist = [10,20,30,40];
Changeme( mylist );
print ( " Out function: ", mylist ) # 这样写也不会影响外部的mylist

# python传入时不指定参数顺序
def printinfo(name, age):
  print(" name: ", name);
  print(" age: ", age);
  return;
# 调用printinfo函数
printinfo( age = 50, name = "runoob" )  # 如果写成printinfo( 50, 'runoob' )则要按顺序

# python传入默认参数，在调用函数时，如果没有传递参数(fortran中的实参)，则会使用默认参数。
def printinfo( name, age = 35 ):
  print ( " name: ", name )
  print ( " age: ", age )
  return
printinfo( age = 50, name = 'luk' )
print ( "--------------------" ) # 当函数中虚参有数值，并且在程序内部过程有输出，只写printinfo()也会输出35
printinfo( name = 'luk' )

# python传入可变长度变量
def printinfo( arg1, *vartuple ):
  print ( " arg1: ", arg1 )
  for var in vartuple:
    print ( " var: ", var )
  return

printinfo ( 10 )
printinfo ( 10, 20, 30 )

# python匿名函数
# 1. python使用lambda来创建匿名函数
# 2. lambda只是一个表达式，函数体比def简单
# 3. lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
sum1 = lambda arg1, arg2: arg1 + arg2
print ( " 10 + 20 = ", sum1( 10, 20 ) )
print ( " 20 + 30 = ", sum1( 20, 30 ) )

# return语句
def sum1( arg1, arg2 ):
  total = arg1 + arg2
  print ( " in function: ", total )
  return total

print ( " out function: ", sum1( 10, 20 ) )

# 变量作用域
# python中，程序的变量并不是哪个位置都可以访问的，访问权限决定于这个变量在哪里赋值
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。python的作用域一共有四种
# 1. L(Local) 局部作用域
# 2. E(Enclosing) 闭包函数外的函数中
# 3. G(Global) 全局作用域
# 4. B(Bulit-in) 内建作用域

x = int(2.9) # 内建作用域
g_count = 0 # 全局作用域
def outer():
  o_count = 1 # 闭包函数外的函数中
  def inner():
    i_count = 2 # 局部作用域

# python中只有模块(module)，类(class)，以及函数(def,lambda)，才会引入新的作用域
# 其他代码块(如if/elif/else/、try/expect、for/while等)是不会引入新的作用域，也就是说这些语句内定义的变量，外部也可以访问

# 下面例子中，msg变量定义在if语句块中，但外部还是可以访问的
if True:
  msg = ' I am lukailiang! '

print ( msg )

# 如果将msg定义在函数中，则它就是局部变量，外部不能访问
def test():
  msg1 = ' error! '

# print ( msg1 ) 这句报错，因为在全局中没定义变量msg1
# 这里值得注意一下，将局部变量与全局变量的命名最好不一致，如果一致，有时会混淆
# 例如，上面如果在函数test中定义为msg，然后再print(msg)，如果全局中定义了msg，就会输出全局中msg的值，而不是函数test中msg的值，这里注意一下

# 全局变量与局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
total = 0; # 这是一个全局变量
def sum( arg1, arg2 ):
  total = arg1 + arg2; # total在这里时局部变量
  print ( " In function total is ", total )
  return total;

# 调用函数sum
sum(10,20)
print ( " Out function total is ", total )
 
# global 和 nonlocal 关键字
num = 1
def fun1():
  global num  # 说明num是全局变量和局部变量，意思是局部变量num改变后，全局变量中的num也会改变
  print ( " before: num = ", num )
  num = 123 # 修改num的值
  print ( " after: num = ", num )

# 调用函数
fun1()

# 如果要修改嵌套作用域(enclosing作用域，外层非全局作用域)中的变量则需要nonlocal关键字
def outer():
  num = 10
  def inner():
    nonlocal num  # nonlocal关键字声明
    num = 100
    print ( " num =  ", num )
  # 调用函数inner
  inner()
  print ( " num = ", num )
# 调用函数outer
outer()

# lambda匿名函数也是可以用“关键字参数”进行参数传递
g = lambda x, y: x**2 + y**2
print ( " g(2,3) = ", g(2,3) )  # 默认为g(x=2, y=3)
print ( " g(y=3,x=2) =  ", g(y=3,x=2) )  # 不选择默认时，需要指定
# 传入一个参数
g = lambda x=0, y=0: x**2 + y**2
print ( " g(2) = ", g(2) )  # 默认为g(x=2)，y值为函数中y的值
print ( " g(y=3) = ", g(y=3) )  # 此时需要指定

# 下面这个例子证明全局变量在局部变量中仍然起作用（但是局部改变后并不影响外部的值），反之则不行
# 如果想通过改变局部变量的值，而改变全局变量的值，需要使用global
b = 1
def ss():
  a = 1 + b
  print ( " a = ", a )
# 第一次调用函数ss()
ss()
# 该变b的值
b = 10
# 再次调用ss()
ss()

# 存在一种特殊情况
a = 10
def test():
  a = a + 1
  print ( " a = ", a )
# test() # 这种情况报错，因为test函数中不能对全局变量a更新


# 注意：函数内能访问全局变量，但不能更新（修改）其值，除非使用global
a = 10
def sum(n):
  n = n + a  # 访问全局变量的值
  # 如果加下面一句会报错
  # a = 1，不能修改全局变量的值
  print ( " a = ", a, end = "," )
  print ( " n = ", n )
sum(3)

# 下面代码是变量作用域的例子
# 1. 局部作用域
x = int(3.3)

x = 0
def outer():
  x = 1
  def inner():
    x = 2
    print ( " x = ", x )  # 执行结果为2，因为在函数inner内部找到了变量x
  inner()
outer()

# 2. 闭包函数外的函数中
x = int(3.3)

x = 0
def outer():
  x = 1
  def inner():
    i = 2
    print ( " x = ", x )  # 在局部变量中找不到，去局部外的局部寻找
  inner()
outer()

# 3. 全局作用域
x = int(3.3)
x = 0
def outer():
  o = 1
  def inner():
    i = 2
    print ( " x = ", x )  # 在局部(inner函数),局部的局部(outer函数)中都没找到，去全局找
  inner()
outer()

# 4. 内建作用域
x = int(3.3)
g = 0
def outer():
  o = 1
  def inner():
    i = 2
    print ( " x = ", x )
  inner()
outer()
