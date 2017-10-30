# -*- coding: utf-8 -*-

b = input(u'enter b')
n = input(u'enter n')
m = input(u'enter m')
tmp_a = 1
tmp_b = b
while n != 0:
    if n & 1 == 1:
        tmp_a = (tmp_a * tmp_b) % m
    tmp_b = (tmp_b ** 2) % m
    n >>= 1
print tmp_a
