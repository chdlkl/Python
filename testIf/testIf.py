# if语句的形式
# if condition_1:
#   statement_block1
# elif condition_2:
#   statement_block2
# else:
#   statement_block3
# 注意事项：
# 1. python中用elif代替了else if，所以if语句的关键字为：if--elif--[elif]--else
# 注意fortran中是：if--else if--[else if]--else--end if
# 2. 每个条件后面都要使用冒号(:),表示接下来是满足条件后要执行的语句块
# 3. 使用缩进划分语句块，一个语句块，缩进必须一致
# 4. python中没有switch-case语句
var1 = 100
if var1:
  print ( ' 1 - if expression is ture ' )
  print ( ' var1 is ', var1 )

var2 = 0 
if var2:
  print ( ' 2 - if expression is ture ' )
else:
  print ( ' 2 - if expression is false ' )

print ( ' Good bye! ' )

# 狗的年龄计算
age = int( input( " please input your dog's age: " ) )
print ( "" )
if age < 0:
  print ( " Are you kidding me ? " )
elif age == 1:
  print ( " eq to 14 years old human! " )
elif age == 2:
  print ( " eq to 22 years old human! " )
elif age > 2:
  humanAge = 22 + ( age - 2 ) * 5
  print ( " eq to human is %d old! " %( humanAge ) )

# if中常用的操作符：>, >=, <, <=, ==, !=(fortran中为/=)

# 数字比较运算
number = 7
guess = -1
print ( ' guess number game: ' )
while guess != number:
  guess = int( input( " please input your guess number: " ) )
  if guess == number:
    print ( ' you are right! ' )
  elif guess < number:
    print ( ' the guess number is less! ' )
  elif guess > number:
    print ( ' the guess number is more! ' )

# if嵌套
# 在嵌套if语句中，可以把if...elif...else结构放在另一个if...elif...else结构中
# if 表达式1:
#   语句
#   if 表达式2:
#     语句
#   elif 表达式3:
#     语句
#   else:
#     语句
# elif 表达式4:
#   语句
# else:
#   语句
num = int( input( " please input a number: " ) )
if num % 2 == 0:
  if num % 3 == 0:
    print ( " the number of input can be devided by 2 and 3! " )
  else:
    print ( " the number of input can be devided by 2 and 3 is not! " )
else:
  if num % 3 == 0:
    print ( " the number of input can be devided by 3 and 2 is not! " )
  else:
    print ( " the number of input can not be devided by 2 and 3! " )

# 例子
import random
x = random.choice( range(100) )  # 随机数0-99
y = random.choice( range(200) )  # 随机数0-199
if x > y:
  print ( ' x : ', x )
elif x == y:
  print ( ' x + y : ', x + y )
else:
  print ( ' y : ', y )

# 一个if对应一个else，但是一个if中可以嵌套多个if

# 数字猜谜游戏优化
print ( " guess number game: " )
a = 1
i = 0
while a != 20:  # 注意冒号
  a = int( input( " please input number: " ) )
  i += 1
  if a == 20:
    if i < 3:
      print ( " 真厉害，这么快就猜对了 " )
    else:
      print ( " 总算猜对了 " )
  elif a < 20:
    print ( " 你猜的数字太小了 " )
  else:
    print ( " 你猜的数字太大了 " )


###  退出提示
input ( " Press the enter! " )



