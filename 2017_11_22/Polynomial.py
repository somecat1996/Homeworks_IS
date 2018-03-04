# coding=UTF-8
import copy

class Polynomial:
    def __init__(self, coe, mod):
        #检查输入
        try:
            if type(coe) != type([]):
                raise TypeError
        except TypeError:
            print u'需要输入一个数组作为系数'
        try:
            if type(mod) != type(1):
                raise TypeError
            if mod < 0:
                raise ValueError
        except TypeError:
            print u'需要输入一个整数作为数域生成元'
        except ValueError:
            print u'生成元不能小于0'

        #将系数取膜
        if mod != 0 and not (len(coe) == 1 and coe[0] == 0):
            first = coe[0]
            while first % mod == 0:
                del coe[0]
                first = coe[0]
                if len(coe) == 1:
                    break
            for i in range(len(coe)):
                coe[i] %= mod

        #储存
        self.coes = coe
        self.deg = len(coe)
        self.mod = mod

    #输出多项式格式字符串
    def __str__(self):
        if self.deg == 1:
            return str(self.coes[0])
        output = ''
        for i in range(-1, -self.deg-1, -1):
            if i == -1 and self.coes[i]:
                output = '+' + str(self.coes[i]) + output
            elif i == -2 and self.coes[i] == 1:
                output = '+' + 'x' + output
            elif i == -2 and self.coes[i] != 1 and self.coes[i] != 0:
                output = '+' + str(self.coes[i]) + 'x' + output
            elif i == -self.deg and self.coes[i] == 1:
                output = 'x^' + str(-i-1) + output
            elif self.coes[i] and self.coes[i] != 1:
                output = '+' + str(self.coes[i]) + 'x^' + str(-i-1) + output
            elif self.coes[i] == 1:
                output = '+' + 'x^' + str(-i - 1) + output
        if output[0] == '+':
            output = output[1:]
        return output

    #相等
    def __eq__(self, other):
        if self.mod == other.mod:
            return False
        if self.deg != other.deg:
            return False
        if self.coes != other.coes:
            return False
        return True

    #加法
    def __add__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        if self.deg > other.deg:
            length = self.deg
        else:
            length = other.deg
        newcoe = [0] * length
        for i in range(-1, -length - 1, -1):
            if i >= -self.deg:
                newcoe[i] += self.coes[i]
            if i >= -other.deg:
                newcoe[i] += other.coes[i]
        return Polynomial(newcoe, self.mod)

    #减法
    def __sub__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        if self.deg > other.deg:
            length = self.deg
        else:
            length = other.deg
        newcoe = [0] * length
        for i in range(-1, -length - 1, -1):
            if i >= -self.deg:
                newcoe[i] += self.coes[i]
            if i >= -other.deg:
                newcoe[i] -= other.coes[i]
        return Polynomial(newcoe, self.mod)

    #乘法
    def __mul__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        newcoe = [0] * (self.deg + other.deg)
        for i in range(-1, -self.deg - 1, -1):
            for j in range(-1, -other.deg - 1, -1):
                newcoe[i+j+1] += self.coes[i] * other.coes[j]
        return Polynomial(newcoe, self.mod)

    #整除
    def __div__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        tmp = []
        n = self.deg
        m = other.deg
        if n < m:
            tmp.append(0)
        else:
            r = copy.copy(self.coes)
            for i in range(-n, -m+1):
                tmp.append(r[i] / other.coes[0])
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coes[k]
        return Polynomial(tmp, self.mod)

    #同余
    def __mod__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        tmp = []
        n = self.deg
        m = other.deg
        if n < m:
            tmp.append(0)
            r = copy.copy(self.coes)
        else:
            r = copy.copy(self.coes)
            for i in range(-n, -m+1):
                tmp.append(r[i] / other.coes[0])
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coes[k]
        return Polynomial(r, self.mod)

#多项式欧几里得除法求最大公因数
def Division(f, g):
    arr = []
    r1 = f
    r2 = g
    while not r1 % r2 == Polynomial([0], f.deg):
        arr.append(r1/r2)
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    s_array = [Polynomial([1], f.mod), Polynomial([0], f.mod)]
    t_array = [Polynomial([0], f.mod), Polynomial([1], f.mod)]
    for i in arr:
        s_array.append(s_array[-2] - i * s_array[-1])
        t_array.append(t_array[-2] - i * t_array[-1])
    return s_array[-1], t_array[-1]
