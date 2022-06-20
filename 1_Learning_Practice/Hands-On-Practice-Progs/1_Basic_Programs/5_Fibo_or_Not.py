def Fibo_Not(n):
    c = 0
    a = 1
    b = 1
    if n == 0 or n == 1:
        print("{} is Fibonacci".format(n))
    else:
        while c < n:
            c = a + b
            b = a
            a = c
        if c == n:
            print("{} is Fibonacci".format(n))
        else:
            print("{} is Not Fibonacci".format(n))


Fibo_Not(25)
