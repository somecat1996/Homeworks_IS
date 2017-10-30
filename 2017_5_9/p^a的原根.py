# coding=UTF-8


def get_a():
    a = 0
    while True:
        if a > 0 and isinstance(a, int):
            break
        a = input("请输入正整数a")
    return a


def get_p():
    p = 0
    while True:
        if is_prime(p) and isinstance(p, int):
            break
        p = input("请输入奇素数p")
    return p


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


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


def get_C(m):
    i = 0
    l = range(1, m)
    while i < len(l):
        r1 = l[i]
        r2 = m
        while r1 % r2 != 0:
            tmp = r1 % r2
            r1 = r2
            r2 = tmp
        if r2 == 1:
            i += 1
        else:
            del l[i]
    return l


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


def main():
    p = get_p()
    a = get_a()
    m = p**a
    c = get_C(m-1)
    g = first(p)
    tmp = []
    for i in c:
        t = g**i % m
        if t not in tmp:
            tmp.append(t)
    tmp.sort()
    for i in tmp:
        print i,
    return


if __name__ == '__main__':
    main()
