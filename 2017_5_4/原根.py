# -*- coding: utf-8 -*-


def is_prime(p):
    for i in range(2, p):
        if p % i == 0:
            return True
    return False


def judge(x, y):
    r1 = y
    r2 = x
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


def first(p):
    a = []
    for i in range(2, p):
        if not judge(i, p):
            a.append(i)
    b = []
    j = 2
    tmp = p - 1
    while j <= p - 1:
        if tmp % j == 0:
            tmp /= j
            if j not in b:
                b.append(j)
        else:
            j += 1
    for i in a:
        flag = True
        for j in b:
            tmp = (p-1)/j
            if i**tmp%p == 1:
                flag = False
        if flag:
            return i

p = 0
while p <= 2 or is_prime(p):
    p = int(input(u'请输入奇素数p：'))
a = [1]
for i in range(1, p):
    if not judge(i, p - 1):
        a.append(i)
b = first(p)
for i in a:
    print b**i%p
