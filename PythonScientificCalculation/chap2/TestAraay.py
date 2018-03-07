# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 09:11:38 2018

@author: luk
"""
import numpy
print ( " The numpy version: ", numpy.__version__ )

import numpy as np
 
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
 
# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))
 
# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
 
# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y) # 跟matlab不同都是点乘
print(np.multiply(x, y))
 
# Inv matrix
print ( "inv(y)", np.linalg.inv(y) )
print ( "y*inv(y)", np.dot(y,np.linalg.inv(y)) )
 
# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
print('-----------------------------------')
# multiply是点乘，dot是矩阵乘法类似matlab里面的乘法
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
 
v = np.array([9,10])
w = np.array([11, 12])
 
# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
 
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
 
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
