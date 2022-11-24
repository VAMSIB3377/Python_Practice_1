# Sum of n Natural Numbers

def sum_n_natural(n):
    """x = 0
    for i in range(1, n+1):
        x = i + x
    return x"""
    s = 0
    s = n*(n+1)//2
    return s

# Sum of Squares of n Natural Numbers

def sum_sqr_n_natural(n):
    x = 0
    for i in range(1, n+1):
        x = i**2 + x
    return x


print(sum_n_natural(10))
print(sum_sqr_n_natural(3))
