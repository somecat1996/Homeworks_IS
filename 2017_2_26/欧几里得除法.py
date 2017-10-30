a = input("enter a:")
b = input("enter b:")
if b == 0:
    print "error"
    exit(1)
else:
    print "q = %d, r = %d" %(a/b, a%b)
raw_input("press any key to exit")