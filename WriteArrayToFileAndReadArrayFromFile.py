# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
a = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
b = np.zeros( [3,3] )
file = open( "test1.txt", "w" )
for i in range( len(a) ):
    for j in range( len(a) ):
        file.write( str(a[i][j]) + '\t')  # \t为制表符
    file.write( '\n' )  # \n为换行
file.close()
print( type(a) )  # numpy.ndarray

b = np.loadtxt( "test1.txt" )
for i in range( len(b) ):
    for j in range( len(b) ):
        print( b[i,j], end = '  ' )
    print( '\n' )
    
print( type(b) )  # numpy.ndarray