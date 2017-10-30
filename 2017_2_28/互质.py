a = input("enter a:")
m = input("enter m:")
if a == 0 and m == 0:
    print "error!"
    exit(1)
elif a == 0 or m == 0:
    print "a and m are not coprime."
else:
    r1 = a
    r2 = m
    while r1 % r2 != 0:
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    if r2 == 1: print "a and m are coprime."
    else: print "a and m are not coprime"
raw_input("press any key to exit")