# -*- coding: utf-8 -*-
import math


def _if(p):
    if p % 2 == 0:
        return True
    for i in range(2, int(math.sqrt(p))):
        if p % i == 0:
            return True
    return False

p = 0
flag = True
while flag:
    p = input(u"请输入奇素数p：")
    flag = _if(p)
a = int(input(u"请输入整数a："))
res = a**((p-1)/2)%p
if res == 1:
    print u"%d是%d的平方剩余" % (a, p)
else:
    print u"%d是%d的平方非剩余" % (a, p)