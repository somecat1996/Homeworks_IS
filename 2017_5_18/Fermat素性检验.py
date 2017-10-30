# coding=UTF-8
import random


def gett():
    t = 0
    while t <= 0 and isinstance(t, int):
        t = input(u"请设置安全参数t：")
    return t


def setn():
    tmp = random.randrange(2**11, 2**13)
    return tmp


def getb(n):
    tmp = random.randrange(2, n - 2)
    return tmp


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


def main():
    t = gett()
    while True:
        n = setn()
        flag = True
        for i in range(t):
            b = 1
            while judge(b, n):
                b = getb(n)
            r = b**(n-1)%n
            if r != 1:
                flag = False
        if flag:
            return n


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = main()
    print n
    print is_prime(n)
