# -*- coding: utf-8 -*-
import math


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
        elif len(i) >= 4:
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
    for i in range(lenth + 1):
        d.append(0)
    for i in tmp:
        d[i] = c[i]
    return d


def devision(a, b):
    tmp = []
    g = []
    n = len(a) - 1
    m = len(b) - 1
    if n < m:
        tmp.append(0)
        r = a
    else:
        r = a
        for i in range(n, m - 1, -1):
            tmp.append(a[i] / b[m])
            for k in range(m + 1):
                r[i - k] = r[i - k] - tmp[-1] * b[m - k]
    for i in range(len(tmp) - 1, -1, -1):
        g.append(tmp[i])
    return g, r


def printlist(a):
    out = ""
    for i in range(len(a) - 1, -1, -1):
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
            else:
                a2 = "^" + str(i)
            if a[i] == 1:
                a1 = ""
            elif a[i] == -1:
                a1 = "-"
            else:
                a1 = str(a[i])
            if len(out) != 0 and a[i] > 0:
                a1 = '+' + a1
            out += a1 + "x" + a2


def getm(m):
    out = []
    for i in range(m + 1):
        out.append(0)
    i = 2
    while i <= m:
        if m % i == 0:
            out[i] += 1
            m /= i
        else:
            i += 1
    return out


def solve(a, q, num):
    out = []
    for i in range(q):
        sum = calculate(a, i)
        if sum % q == 0:
            out.append(i)
    a_ = []
    for i in range(1, len(a)):
        a_.append(a[i] * i)
    if num > 1:
        for i in range(len(out)):
            out[i] = solve_1(a, a_, num, out[i], q)
    return out


def calculate(a, x):
    f = 0
    for i in range(len(a)):
        f += a[i] * x ** i
    return f


def solve_1(a, a_, num, ans, q):
    f_ = calculate(a_, ans)
    d = get_d(q, f_) % q
    for i in range(1, num):
        t = -calculate(a, ans) * d / (q ** i) % q
        ans = ans + t * q ** i % (q ** (i + 1))
    return ans


def get_d(n, e):
    q_array = []
    r1 = n
    r2 = e
    while r1 % r2 != 0:
        q_array.append(r1 / r2)
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    s_array = [1, 0]
    t_array = [0, 1]
    for i in q_array:
        s_array.append(-i * s_array[-1] + s_array[-2])
        t_array.append(-i * t_array[-1] + t_array[-2])
    return t_array[-1]


def final(ans):
    m = ans.keys()
    b = ans.values()
    out = []
    M = []
    tmp1 = 1
    for i in m:
        tmp1 *= i
    for i in m:
        M.append(tmp1 / i)
    M_ = []
    for i in range(len(m)):
        M_.append(get_d(m[i], M[i]) % m[i])
    tmp2 = [[]]
    for i in b:
        tmp_tmp = tmp2
        tmp2 = []
        for j in i:
            for k in tmp_tmp:
                tmp2.append(copy(k, j))
    for i in tmp2:
        tmp_n = 0
        for j in range(len(i)):
            tmp_n += i[j] * M[j] * M_[j]
        out.append(tmp_n)
    return out


def copy(a, b):
    tmp = []
    for i in a:
        tmp.append(i)
    tmp.append(b)
    return tmp


a = get_duoxiangshi("请输入一个多项式")
tmp = []
for i in a:
    tmp.append(i)
m = input("请输入m：")
b = []
for i in range(m + 1):
    if i == 1:
        b.append(-1)
    elif i == m:
        b.append(1)
    else:
        b.append(0)
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
q = getm(m)
solution = {}
for i in range(len(q)):
    if q[i] != 0:
        solution[i ** q[i]] = solve(r, i, q[i])
print solution
ans = final(solution)
for i in range(len(ans)):
    ans[i] %= m
print ans
