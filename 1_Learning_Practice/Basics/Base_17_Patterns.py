"""
for i in range(5):
    for j in range(5):
        print("#", end=" ")
    print()
"""
"""
for i in range(5):
    for j in range(i+1):
        print("#", end=" ")
    print()
    
"""
"""
for i in range(5):
    for j in range(5-i):
        print("#", end=" ")
    print()
"""

"""
for i in range(0, 6):
    for j in range(6, 0, -1):
        if j > i:
            print(" ", end =" ")
        else:
            print("#", end=" ")
    print()
"""

# Assignments

# 1. 1 2 3 4
#    2 3 4
#    3 4
#    4

"""
for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()

"""


# 2. A P Q R
#    A B Q R
#    A B C R
#    A B C D



for i in range(5):
    for j in range(65, 65 + i):
        a = chr(j)
        print(a, end=" ")


    print()

