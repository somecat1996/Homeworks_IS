# -*- coding: utf-8 -*-

def get_e(m, a):
    i = 1
    while True:
        if a**i%m == 1:
            return i
        i += 1


def judge(m, a):
    r1 = a
    r2 = m
    if r1 % r2 == 0 or r2 % r1 == 0:
        return True
    while r1 % r2 != 0:
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    if r2 == 1:
        return False
    else:
        return True

m = 0
while m <= 0 or m % 2 == 0:
    m = int(input(u'请输入奇素数p：'))
a = 0
while a <= 0 or judge(m, a):
    a = input(u'请输入与m互素的a：')
print get_e(m, a)