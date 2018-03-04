from Polynomial import *

# for m in [7, 5, 2]:
#     a1 = Polynomial([1, 5, 4, 3, 0, 1, 3], m)
#     a2 = Polynomial([1, 3, 5, 6, 0, 2, 1], m)
#     print a1 + a2
#     print a1 * a2
#     print a1 * a1
#     print

# a1 = Polynomial([0], 2)
# print a1

t1 = [1, 0, 0, 1, 1]
a1 = Polynomial(t1, 2)
t2 = [1, 0, 0, 0, 1, 1, 0, 1, 1]
a2 = Polynomial(t2, 2)
print a1
print a2
s, t = Division(a1, a2)
print '(', s, ')*(', a1, ')+(', t, ')*(', a2, ')=', s*a1+t*a2
