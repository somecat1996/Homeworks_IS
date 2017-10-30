# -*- coding: utf-8 -*-
import math


def _if(p):
    if p % 2 == 0 or p < 0:
        return True
    for i in range(2, int(math.sqrt(p) + 1)):
        if p % i == 0:
            return True
    return False

def find(p):
    i = 0
    while True:
        if i**2 % p == p - 1:
            return i
        i += 1

def solve(p):
    x = find(p)
    y = 1
    m = (x ** 2 + y ** 2) / p
    i = 0
    while m != 1:
        u = x % m
        v = y % m
        print u'第%d次循环：' % i
        print 'x = %d' % x
        print 'y = %d' % y
        print 'm = %d' % m
        print 'u = %d' % u
        print 'v = %d' % v
        tmp_x = (u * x + v * y) / m
        tmp_y = (u * y - v * x) / m
        x, y = tmp_x, tmp_y
        m = (x ** 2 + y ** 2) / p
        i += 1
    print u'解为：'
    print 'x = %d, y = %d' % (x, y)
    return


p = 0
flag = True
while flag:
    p = input(u"请输入奇素数p：")
    flag = _if(p)
if p != 2 and (p - 1) % 4 != 0:
    print u'无解'
else:
    solve(p)
