import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
# 画三维图
x, y = np.mgrid[-2:2:100j, -2:2:100j]
z = x * np.exp( -x**2 - y**2 )
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap = 'rainbow')

plt.title("z=x*exp(-x^2-y^2)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.ylim(-2.0,2.0)
plt.legend()
plt.show()

# 画一维图
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

# -------------------------------------------------------
# 兼容MATLAB代码风格API
# 1. 绘制曲线图
from matplotlib import pylab
import numpy as np
x = np.linspace(0,10,20)
y = x * x + 2
pylab.plot( x, y, 'r' )  # 'r'代表red
plt.show()


# 2. 使用subplot
pylab.subplot(1,2,1)  # 括号中的内容代表(行，列，索引)
pylab.plot( x, y, 'r--' )  # ''中的内容确定颜色和线型

pylab.subplot(1,2,2)
pylab.plot( y, x, 'g*-' )
plt.show()

# -------------------------------------------------------
# Matplotlib面向对象API(推荐这样画图)
# """使用matplotlib提供的面向对象API，需要导入pyplot模块，并约定为plt
from matplotlib import pyplot as plt
# 使用plt.subplots()添加画布
fig, axes = plt.subplots()
axes.plot( x, y, 'b--' )
plt.show()

# 调整画布尺寸和显示精度
fig, axes = plt.subplots( figsize=(16,9), dpi=50 )  # figsize调整尺寸，dpi调整精度
axes.plot( x, y, 'g-*' )
plt.show()

# 2.1 图名称、坐标轴名称、图例
fig, axes = plt.subplots()

axes.plot(x, x**2, 'r--')
axes.plot(x, x**3, 'b-*')

ax.set_title( "title" )  # 设置图标题
ax.set_xlabel("x lable")  # 设置坐标轴名称
ax.set_ylabel("y lable")

axes.legend( ["y = x^2", "y = x^3"], loc = 2 )  # 设置图例
plt.show()





