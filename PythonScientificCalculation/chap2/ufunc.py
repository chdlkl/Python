import numpy as np
x = np.linspace( 0, 2*np.pi, 10 )
y = np.sin( x )  # ufunc函数产生的结果为数组
z = np.sin( x, out = x )  # 使用out将计算的结果存储在x数组中
