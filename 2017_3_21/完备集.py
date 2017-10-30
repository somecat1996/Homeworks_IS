# coding=UTF-8

m = input("请输入正整数m")
while m <= 0:
    m = input("请输入正整数m")
a = input("请输入整数a")
while a - a*1 != 0:
    a = input("请输入整数a")
b = input("请输入整数b")
while b - b*1 != 0:
    b = input("请输入整数b")

print "Ca = {%d + k*%d}" %(a, m)
print "Cb = {%d + k*%d}" %(b, m)
print "Ca+b = {%d + k*%d}" %(a+b, m)
print "Ca*b = {%d + k*%d}" %(a*b, m)