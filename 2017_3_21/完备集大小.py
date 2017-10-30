# coding=UTF-8

m = 0
while True:
    if m > 0 and type(m) == type(1):
        break
    m = input("请输入正整数m")
i = 0
a = range(1, m)
while i < len(a):
    r1 = a[i]
    r2 = m
    while r1 % r2 != 0:
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    if r2 == 1:
        i += 1
    else:
        del a[i]

print "结果为%d"%(len(a))