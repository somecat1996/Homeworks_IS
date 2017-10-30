# coding=UTF-8


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
            if i**tmp % p == 1:
                flag = False
        if flag:
            return i


def main():
    p = get_p()
    g = first(p)
    length = p - 1
    tmp = []
    i = 0
    while i <= length:
        tmp.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        i += 10
    for i in range(1, p):
        t = g**i % p
        y = t / 10
        x = t % 10
        tmp[y][x] = i
    print '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9'
    for i in range(len(tmp)):
        print str(i)+'\t',
        for j in tmp[i]:
            if j == 0:
                print '\t',
            else:
                print str(j)+'\t',
        print
    while True:
        a = input("请输入正整数a（非正数视为终止）：")
        b = input("请输入正整数b（非正数视为终止）：")
        if a <= 0 or b <= 0:
            break
        a_t = tmp[a % p/10][a % p % 10]
        b_t = tmp[b % p/10][b % p % 10]
        print 'a * b (mod p)= '+str(g**((a_t+b_t) % (p-1)) % p)
        print 'a ^ b (mod p)= ' + str(g ** ((a_t*b) % (p - 1)) % p)
    return


if __name__ == '__main__':
    main()
