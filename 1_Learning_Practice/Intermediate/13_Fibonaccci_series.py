

def fibo():
    n1 = 0
    n2 = 1
    lst = []
    lst.append(n1)
    lst.append(n2)
    for i in range(20):
        n3 = n1 + n2
        n1, n2 = n2, n3
        if n3 > 100:
            break
        else:
            lst.append(n3)
    return lst



def fibo_rec(n):
    if n <= 1:
        return n
    else:
        return (fibo_rec(n-1)+fibo_rec(n-2))

for i in range(10):
    print(fibo_rec(i))



print(fibo())

