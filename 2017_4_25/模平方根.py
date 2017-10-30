# -*- coding: utf-8 -*-
def solve(p, q):
    p_ = 0
    while p*p_ % q != 1:
        p_ += 1
    print 'p_ = %d' % p_
    t = 0
    s = q - 1
    while s%2 == 0:
        t += 1
        s /= 2
    print 't = %d' % t
    print 's = %d' % s
    n = 2
    while youjie(n, q):
        n += 1
    print 'n = %d' % n
    b = n**s % q
    print 'b = %d' % b
    x = p**((s + 1)/2)%q
    for i in range(t - 1):
        print 'x(%d) = %d' % (t-1-i, x)
        e = (p_*x**2)**(2**(t - 2 - i))%q
        print '(p_*x**2)**(2**(%d))%%q = %d' % (t - 2 - i, e)
        if e == 1:
            pass
        else:
            x = x*b**(2**i) % q
    return x


def youjie(p, q):
    a = []
    tmp = p
    i = 2
    while i <= p:
        if tmp % i == 0:
            a.append(i)
            tmp /= i
        else:
            i += 1
    ans = 1
    for i in a:
        result = 1
        top = i
        buttom = q
        while top != 1 and top != -1 and top != 2:
            result *= (-1)**(((top - 1)/2)*((buttom - 1)/2))
            top, buttom = buttom % top, top
        if top == -1:
            result *= (-1)**((buttom - 1)/2)
        elif top == 2:
            result *= (-1) ** ((buttom**2 - 1) / 8)
        ans *= result
    if ans == 1:
        return True
    else:
        return False

p = input(u"请输入p")
q = input(u"请输入q")
if youjie(p, q):
    print u"有解"
    print solve(p, q)
else:
    print u'无解'