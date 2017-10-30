a = input("enter a:")
b = input("enter b:")
if a == 0 and b == 0:
    print "error!"
    exit(1)
elif a == 0 or b == 0:
    if a == 0:print b
    else:print a
else:
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    print r2
raw_input("press any key to exit")