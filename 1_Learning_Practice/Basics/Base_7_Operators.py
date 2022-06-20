# 1. Arithmetic Operators -> (+, -, *, /, %)
# 2. Assignment Operators -> (=, +=, -=, *=, /=)
# 3. Relational Operators -> (<, >, <=, >=)
# 4. Logical Operators    -> (and, or, not)
# 5. Unary Operators      -> ( Negations ) -> Mentioning Arithmetic Sign either + or -


# 1. Arithmetic

x = 5
y = 3

add = x + y
sub = x - y
mul = x * y
div = x / y
mod = x % y

print(add)
print(sub)
print(mul)
print(div)
print(mod)
print("\n\n")


# 2. Assignment

a = 2
print(a)

a += 3
print(a)

a -= 2
print(a)

a *= 4
print(a)

a /= 3
print(a)

print("\n\n")


# 3.Relational Operators

m = 10
n = 20

print(m > n)

print(m < n)

print(m >= n)

print(m <= n)

print("\n\n")

# 4. Logical

u = 13
v = 23

if u > 10 and v < 20:
    print("Value is Between 10 and 20")

elif u > 10 or v > 10:
    print("Either of U or V is Greater Than 10")

else:
    print("Nothing")

print("\n\n")


# 5. Unary

z = 10
print(z)

z = -z
print(z)

z = -z
print(z)