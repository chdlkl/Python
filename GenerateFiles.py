import os
n = 10;
for i in range(n):
    tmp = str(i)+'.txt'
    os.system( "cp > "+tmp )
