a = 5
b = 6

print(a, b)


# 1. Swapping Without Using Third Variable

a, b = b, a
print(a, b)

# 2. Swapping Without Using Third Variable and By Using a Formula
a = a ^ b     # 11
b = a ^ b     # 6
a = a ^ b     # 5

print(a, b)


# 3. Swapping Using Third ( Temp ) Variable

temp = a
a = b
b = temp

print(a,b)


