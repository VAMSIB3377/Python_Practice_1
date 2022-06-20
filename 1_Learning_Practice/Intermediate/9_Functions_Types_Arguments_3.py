# Types of Arguments
# 1. Formal Arguments -> Position
#                     -> Keyword
#                     -> Default
#                     -> Variable Length

# 2. Actual Arguments


"""
def add(a, b):
    c = a + b
    print(c)


add(5, 6)
"""

# Positional

def person1(name, age):
    print(name)
    print(age)


person1('Vamsi', 22)


# Keyword

def person2(name, age):
    print(name)
    print(age)


person2(age=22, name='Vamsi')



# Default

def person3(name, age=18):
    print(name)
    print(age)


person3(name='Vamsi')
person2(age=22, name='Vamsi')



# Variable Length

print("\n\n")
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


sum(2, 3, 4, 5, 6)

