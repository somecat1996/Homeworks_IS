# -*- coding: utf-8 -*-
def get_duoxiangshi(announce):
    a = raw_input(announce)
    b = a.split('+')
    c = {}
    for i in b:
        if len(i) == 1:
            try:
                c[0] = int(i)
            except:
                c[1] = 1
        elif len(i) == 4:
            d = i.split("x^")
            c[int(d[1])] = int(int(d[0]))
        elif len(i) == 3:
            d = i[2]
            c[int(d)] = 1
        elif len(i) == 2:
            d = i[0]
            c[1] = int(d)
        else:
            print 'error'
            return
    tmp = c.keys()
    lenth = max(tmp)
    d = []
    for i in range(lenth+1):
        d.append(0)
    for i in tmp:
        d[i] = c[i]
    return d

def devision(a, b):
    tmp = []
    g = []
    n = len(a)-1
    m = len(b)-1
    if n < m:
        tmp.append(0)
        r = a
    else:
        r = a
        for i in range(n, m-1, -1):
            tmp.append(a[i]/b[m])
            for k in range(m+1):
                r[i-k] = r[i-k]-tmp[-1]*b[m-k]
    for i in range(len(tmp)-1, -1, -1):
        g.append(tmp[i])
    return g, r

def printlist(a):
    out = ""
    for i in range(len(a)-1, -1, -1):
        if i == 0:
            if a[i] > 0 and len(out) != 0:
                out += '+' + str(a[i])
            elif a[i] < 0 and len(out) != 0:
                out += '-' + str(a[i])
            elif a[i] != 0:
                out += str(a[i])
            return out
        if a[i] != 0:
            if i == 1:
                a2 = ""
            else:a2 = "^" + str(i)
            if a[i] == 1:
                a1 = ""
            elif a[i] == -1:
                a1 = "-"
            else:a1 = str(a[i])
            if len(out) != 0 and a[i] > 0:
                a1 = '+' + a1
            out += a1 + "x" + a2



a = get_duoxiangshi(u"请输入一个多项式：")
tmp = []
for i in a:
    tmp.append(i)
b = get_duoxiangshi(u"请输入另一个多项式：")
g, r = devision(a, b)
a1 = printlist(tmp)
b1 = printlist(b)
g1 = printlist(g)
r1 = printlist(r)
if g1 == "1":
    g1 = ""
else:
    g1 = "(" + g1 + ")"
if r1 == "":
    r1 = "0"
print a1 + "=" + g1 + "(" + b1 + ")+" + r1