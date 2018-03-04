from Polynomial import *

# g = Polynomial([1, 1, 0, 1, 0, 1, 1, 0], 2)
# f = Polynomial([1, 0, 0, 0, 1, 1, 1, 0, 1], 2)
# q = g*g*g
#
# print q%f
f = Polynomial([1, 0, 0, 0, 1, 1, 1, 0, 1], 2)
x = Polynomial([1, 0, 0, 0, 1, 0, 0], 2)
y = Polynomial([1, 0, 1, 0], 2)
print (y*y+x*y)%f
print (x*x*x+x*x+Polynomial([1], 2))%f