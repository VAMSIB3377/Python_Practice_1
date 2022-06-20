num = 5

# 5 is storing into a variable named as num
# which will have some specific address
# We can find address of a variable using the id() function Ex:- id (num)

print(id(num))

name = 'abc'
print(id(name))

a = 10
b = a

print("\n\n")

print(id(a))
print(id(b))
print(id(10))

x = 10

print(id(x))

print(type(x))