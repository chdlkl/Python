# 数字类型转换
a = 1.2 
print ( 'after transport 1.2 is ', int(a) )
b = 5
print ( 'after transport 5 is ', float(b) )
print ( 'after transport 1.2 and 5 to complex is ', complex(a,b) )

# python 中整数除法总是返回浮点型数据，Fortran中整数相除返回整数
print ( '7 / 3 is ', 7 / 3 )

# 如果要使用数学函数以及pi与e，需要先import math
import math
print ( 'pi is ', math.pi )
print ( 'e is ', math.e )
print ( 'sin(pi/2) is ', math.sin( math.pi/2 ) )

# 这里还要指出一下，python中的取绝对值函数为fabs，与Fortran中的abs不同
print ( '|-3.1| is ', math.fabs(-3.1) )
