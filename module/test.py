# 把定义的函数和变量放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块
# 模块是一个包含了你定义的函数和变量的文件，后缀名为.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
# import 语句
# 想使用python源文件，只需在另一个源文件里执行import语句，语法如下：
# import module1[,module2[,...moduleN]]
# 当解释器遇到import语句，如果模块在当前的搜索路径就会被导入
# 例子
# 导入模块
import support
# 调用模块里包含的函数
support.print_func( " luk " )

import fibo
print ( dir( fibo ) )   # 用dir()函数可以找到模块内定义的所有名称

fibo.fib( 1000 )
print ( fibo.fib2( 100 ) ) 

print ( ' fiboName: ', fibo.__name__ )

# 如果打算经常使用一个函数，可以把它赋给一个本地名称
testfib = fibo.fib
testfib( 500 )

# from...import语句
# python的from语句让你从模块中导入一个指定的部分到当前的命名空间中，语法如下：
# from modname import name1[,name2[,...nameN]]
# 例如要导入模块fibo中的fib函数
# from fibo import fib, fib2
# fib ( 500 )
# 上面的声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的函数fib引入进来

# from ...import*语句
# 把一个模块的所有内容全都导入到当前的命名空间
# from modname import* 这种声明不该被过多使用

# 每一个模块都有一个__name__属性，当其值是'__main__'时，表示该模块自身在运行，否则是被引入

import using_name


