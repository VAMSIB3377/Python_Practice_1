# Factorial of a Number


# n = int(input("Enter The Number That You Want to Find The Factorial Of : "))
# x = 1
# for i in range(1, n+1):
#    x = x*i
# print(x)


# Using Recursion

def fact(n):
    if n < 0:
        return "Negative Number"
    elif n == 1:
        return 1
    else:
        return n*fact(n-1)


x = int(input("Enter The Number That You Want to Find The Factorial Of : "))
print(fact(x))
