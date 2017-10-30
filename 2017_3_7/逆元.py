a = input("enter a:")
b = input("enter b:")
c = input("enter c:")
if a == 0 or b == 0:
    print "error!"
    exit(1)
else:
    q_array = []
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        q_array.append(r1/r2)
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    s_array = [1, 0]
    t_array = [0, 1]
    for i in q_array:
        s_array.append(-i * s_array[-1] + s_array[-2])
        t_array.append(-i * t_array[-1] + t_array[-2])
    if c%r2 != 0:
        print "unsolvable"
    else:
        print "particular solution: x=",s_array[-1], "  y=", t_array[-1]
        print "general solution: x =", s_array[-1], "- t *", b/r2, "; y =", t_array[-1], "+ t *", a/r2
raw_input("press any key to exit")