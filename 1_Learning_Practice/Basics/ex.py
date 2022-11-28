def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n = 5
print("Factorial of {0} is {1}".format(n, fact(n)))