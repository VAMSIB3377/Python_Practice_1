
"""
i = 0
while i < 5:
    print("Hello")
    i += 1


i = 5
while i>=1:
    print("Hello")
    i -= 1



i = 1
while i <= 5:
    print("Vamsi  ", i)
    i += 1




i = 1
while i <= 5:
    print("Vamsi ", end="")
    j = 1
    while j <= 4:
        print("Rocks ", end="")

        j += 1

    print()

    i += 1


"""

# Assigments

# 1. Write a code to print all the values from 1 to 100.
#    Skip the number which are divisible by 3 or 5

i = 1
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        print(i)
    i += 1

print("\n\n")


# 2. Write a Code to Print The Below Pattern
"""

# # # # #
# # # # #
# # # # #
# # # # #

"""

a = 0
while a < 4:
    b = 0
    while b < 5:
        print("# ", end="")
        b += 1
    a += 1
    print()
