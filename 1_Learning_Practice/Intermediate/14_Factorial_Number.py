def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


def fact_rec(n):
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)


print(factorial(4))

print(fact_rec(5))
