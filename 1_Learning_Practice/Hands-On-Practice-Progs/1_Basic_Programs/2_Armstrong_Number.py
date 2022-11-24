def Armstrong(n):
    a = str(n)
    x = 0
    for i in a:
        x = (int(i)**3)+x
        # t = n%10
        # x = (t * t * t) + x
        # t = t//10
    if x == n:
        print("{} is an Armstrong Number".format(n))
    else:
        print("{} is Not an Armstrong Number".format(n))


Armstrong(153)
