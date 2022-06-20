# 1. None       -> When a Variable is not assigned None to it then it is Called as None Type
# 2. Numeric    -> A. int       --> Integer Data
#               -> B. float     --> Floating Point Data or Decimal Values
#               -> C. Complex   --> Combination of Variables or Values with alphabets   Ex:- a+bj or 6+9j
#               -> D. bool      --> True or False
# 3. List       -> Collection of a List of Elements of any Data Type and It is Mutable
# 4. Tuple      -> Collection of Different Types of Elements Which will be Immutable
# 5. Set        -> Set is a Collection of Non-Duplicate Data and it is also Immutable
# 6. String     -> String is Data Type Which is used to represent String Type of Data and it is Immutable
# 7. Range      -> Range Function Only works with integers or whole numbers. It will give output
# of the integers range that we select
# 8. Dictionary -> It is set of Key-Value Pairs and it does not allow duplicate Values and Dictionaries are Unordered

a = None
print(type(a))

a = 2
print(type(a))

f = 5.4
print(type(f))

a = 5+6j
print(type(a))

a = True
print(type(a))

a = [1, 2, 3, 4, 5, 6]
print(type(a))

a = (1, 2, 3, 4, 5)
print(type(a))

a = {7, 6, 5, 4, 3, 2}
print(type(a))

a = {1 : "abc", 2:"bcd", 3:"cde"}
print(type(a))

x = int(f)
print(type(x))

f1 = float(x)
print(type(f1))

s = 5>6
print(s)

print(range(10))
print(list(range(10)))