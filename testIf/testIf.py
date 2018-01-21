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




###  退出提示
input ( " Press the enter! " )



