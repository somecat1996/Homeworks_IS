import random


def get_prime(num1, num2):
    array = range(2, num2)
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            if array[j] % array[i] == 0:
                del array[j]
            else:
                j += 1
        i += 1
    j = 0
    while j < len(array):
        if array[j] < num1:
            del array[j]
        else:
            j += 1
    return array


def if_prime(a, b):
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    return r2 == 1


def get_e(p, q):
    tmp = (p - 1) * (q - 1)
    e = random.randint(0, tmp)
    while not if_prime(e, tmp):
        e = random.randint(0, tmp)
    return e


def get_d(p, q, e):
    q_array = []
    r1 = (p - 1) * (q - 1)
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


def code(m, e, n):
    m1 = []
    for i in m:
        m1.append(int(mod(i, e, n)))
    return m1


def decode(m1, d, n):
    m2 = []
    for i in m1:
        m2.append(int(mod(i, d, n)))
    return m2


def mod(b, n, m):
    tmp_a = 1
    tmp_b = b
    while n != 0:
        if n & 1 == 1:
            tmp_a = (tmp_a * tmp_b) % m
        tmp_b = (tmp_b ** 2) % m
        n >>= 1
    return tmp_a


def main():
    prime_list = get_prime(2 ** 13, 2 ** 14)
    d = -1
    while d < 0:
        p = random.choice(prime_list)
        q = random.choice(prime_list)
        n = p * q
        e = get_e(p, q)
        d = get_d(p, q, e)
    print 'p = %d' % p
    print 'q = %d' % q
    print 'n = %d' % n
    print 'e = %d' % e
    print 'd = %d' % d
    message = "Mathmatical Fundation of Information security + 20170322 + 515030910195"
    print "message = " + message
    m = map(ord, message)
    print "m = ", m
    m1 = code(m, e, n)
    print "m1 = ", m1
    m2 = decode(m1, d, n)
    print "m2 = ", m2
    m3 = map(chr, m2)
    m4 = ''
    for i in m3:
        m4 += i
    print "m4 = ", m4


if __name__ == "__main__":
    main()
