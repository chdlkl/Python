# 列表的使用方法
# 1. 添加元素
list1 = [1,2,3,4];
list1.append(5);  # list1.append(x)在列表后添加元素x，这种方法每次只能添加一个
print ( " list1: ", list1 )

list2 = [1,2,3,4];
list2[len(list2):] = [5,6,7];  # 这种也是向列表后添加元素，这种方法可以一次添加多个元素
print ( " list2: ", list2 )

# 2. 列表扩充
list3 = list2[:];  # 这里要特别注意，如果写成list3 = list2，则在后面改变两者中的任一个，另一个也会改变
list3.extend( list2 );  # 相当于list3[len(list3):] = list2
print ( " list3: ", list3 )

# 3. 在指定位置插入一个元素
list3.insert(0,0); # 在list3第一个位置插入0
list3.insert(len(list3),100)  # 在list3最后一个位置插入100, 相当于list3.append(100)和list3[len(list3):] = [100]
print ( " list3: ", list3 )

# 4. list.remove(x):删除列表中值为x的第一个元素。如果没有这样的元素，就会返回一个错误
list3.remove(0);
print ( " list3: ", list3 )

# 5. 从列表指定位置删除元素，并将其返回。如果没有指定索引，list.pop()返回最后一个元素，元素随机从列表中删除
list3.pop(len(list3)-1);  # 删除最后一个元素
print ( " list3: ", list3 )

# 6. list.clear()移除列表中的所有项，等于del list[:]，注意del list则是删除整个列表
list3.clear()
print ( " list3: ", list3 )
print ( " list3 has been cleared! " )

# 7. list.index(x):返回列表中第一个值为x的索引。如果没有该元素就会返回一个错误
print ( " list2: ", list2 )
print ( " list2.index(3): ", list2.index(3) )

# 8. list.count(x): 返回x在列表中出现的次数
num = list2.count(2)
print ( " list2.count(2) ", num ) 

# 9. list.reverse(): 倒排列表中的元素
list2.reverse() # 不带参数的语句要单独写一行
print ( " list2.reverse() ", list2 ) 

# 10. list.sort(): 排序
list2.sort()
print ( " list2.sort(): ", list2 )

# 11. list.copy(): 复制列表list，相当于list1 = list[:]
list3 = list2.copy();
print ( " list3: ", list3 )

# 将列表当堆栈使用
# 堆栈:最先进入的元素最后一个被释放（先进后出）
# 用append()的方法可以把一个元素添加至堆栈顶，用不指定索引的pop()方法可以把一个元素从堆栈顶释放
stack = [3,4,5]
stack.append(6); # 尾部添加元素6
stack.append(7); # 尾部添加元素7
print ( " stack: ", stack )
stack.pop() # pop()不指定索引位置时，释放最后一个元素
print ( " stack: ", stack )

# 不建议将列表当作队列使用

# 列表推导式

vec = [1,2,3];
vec = [3*x for x in vec]
print ( " vec = ", vec )

vec = [ [x,x**2] for x in vec ]
print ( " vec = ", vec )
print ( " vec[1][1] = ", vec[1][1] )

# 用x.strip()函数去掉列表中字符串两端的空格
freshfruit = [ '  banana', ' loganberry ', 'passion fruit  ' ];
freshfruit = [ x.strip() for x in freshfruit ]
print ( " freshfruit: ", freshfruit )

# 用if子句作为过滤器，像Fortran中的forall语句
# vec = [2,3,4]
# 这里要注意，如果vec是一维向量，则下面语句写if>某个数
# 如果vec是一个二维数组，2*x作用于子列表，表示输出两次，并不是给每个数字乘以2，如果不满足，则清楚不满足条件的列表元素
vec = [ 2*x for x in vec if x > [3,10] ] 
print ( " vec = ", vec )

vec1 = [2,4,6]
vec2 = [4,3,-9]
vec = [x*y for x in vec1 for y in vec2]  # vec1中的每个元素都和vec2中的每个元素相乘
print ( " vec = ", vec )
vec = [x+y for x in vec1 for y in vec2] # vec1中的每个元素都和vec2中的每个元素相加
print ( " vec = ", vec )
# 对应元素相加
vec = [vec1[i]*vec2[i] for i in range(len(vec1))] # range()函数真是好用
print ( " vec = ", vec )

# 重点：嵌套列表解析
matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
matrix1 = matrix
# 求其转置
trans = []
tmp = []
for i in range(4):
  for j in range(3):
    tmp.append( matrix[j][i] )
  trans.append(tmp)
  tmp =  []
print ( trans )
# 也可以用下面的代码
# trans = []
# for i in range(4):
#   tmp = []
#   for row in matrix:
#     tmp.append(row[i])
#   trans.append(tmp)
# 或者
# print ( [[row[i] for row in matrix1] for i in range(4)] )  

# del语句
# 使用del语句可以从列表中依据索引来删除一个元素。
a = [-1,1,66.25,333,333,1234.5]
del a[0]
print ( " a: ", a )
del a[2:4]
print ( " a: ", a )
del a[:] # 清空列表
print ( " a: ", a )
# 语句del a删除实体变量，引用报出错

# 元组和序列
# 元组在整体输出时总是有括号的，在输入时括号可有可无
# 输出元组中的单个元素时，没有括号
t = 12, 54, 'hello'
print ( " t[0]: ", t[0] )
print ( " t: ", t )
u = t, ( 1, 2, 3, 4, 5 )
print ( " u: ", u )

# 集合：是一个无序不重复元素的集合。基本功能包括关系测试和消除重复元素
# 可以使用大括号{}创建集合。注意：如果要创建一个空集合，必须使用set()而不是{}
# {}是创建一个空字典
basket = { 'apple', 'orange', 'pear', 'apple' }
print ( " basket: ", basket ) # 删除重复的元素
if 'orange' in basket:  # 检测成员
  print ( " orange in basket! " )
else:
  print ( " orange not in basket! " )

a = set( 'abcdaedf' ) # 使用set()函数将其转化为集合，删除重复元素
b = set( 'alacazam' )
print ( " a: ", a )
print ( " b: ", b )
print ( " a - b ", a - b ) # 在a中的字母，但不在b中
print ( " a | b ", a | b ) # 在a或b中的字母，并集
print ( " a & b ", a & b ) # 在a和b中都有的字母
print ( " a ^ b ", a ^ b ) # 在a或b中的字母，但不同时在a和b中
# 集合也支持推导式
a = { x for x in 'abracada' if x not in 'abc' }

# 字典
tel = { 'jack': 4098, 'sape': 4139 }
tel['guide'] = 4127 # 添加元素
print ( " tel: ", tel )
del tel['sape'] # 删除元素
tel['irv'] = 4127
print ( " tel: ", tel )

list1 = list( tel.keys() ) # 将字典的键值转化为列表
print ( " list1: ", list1 )
list1 = sorted( tel.keys() ) # 用sorted()对字典的键值排序
print ( " list1: ", list1 )
list1 = sorted( tel.values() ) # 用sorted()对字典的值排序
print ( " list1: ", list1 )

# 字典推导式
{ x: x**2 for x in (2, 4, 6) }

# 使用关键字参数指定键值对
dict( sape = 4123, guido = 1234, jack = 2435 )

int() # 整数 
float() # 浮点数
str() # 字符串函数
tuple() # 元组函数
list() # 列表函数
dict() # 字典函数
set() # 集合函数

# 遍历技巧，重点
# 在字典中遍历时，关键字和对应的值可以使用items()方法同时读出来
knigths = { 'luk': 24, 'xxx': 25 }
for k, v in knigths.items():
  print ( k, v )

# 在列表中遍历时，索引值和对应值可以使用enumerate()函数
list1 = ['a','b','c','d']
for i, v in enumerate(list1):
  print ( ' i = ', i, ',', ' v = ', v )

# 要反向遍历一个range()序列，首先指定这个序列，然后调用reversed()函数
for i in reversed( range(0,11) ):
  print ( " i = ", i )

# 同时遍历两个或多个列表，可以使用zip()组合
que = [ 'name', 'quest', 'favorite color' ]
ans = [ 'luk', 'the holy grail', 'blue' ]
for q, a in zip( que, ans ):
  print ( "What is your {0}? It is {1}" .format(q,a) )
  # 也可写成
  print ( "What is your %s? It is %s" %(q,a) )
  

