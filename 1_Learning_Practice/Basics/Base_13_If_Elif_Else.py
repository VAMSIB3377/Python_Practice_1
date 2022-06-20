"""
a = 22
if a % 2 == 0:
    print("Even")
    if a > 10:
        print("Greater Than 10")
    else:
        print("Less Than 10")
else:
    print("Odd")

print("Bye")


x = 2
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
elif x == 4:
    print("Four")
else:
    print("Greater Than 4")
"""

# Assignments

# 1. Write a code to check a given number is positive or negative
n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

print("\n\n")

# 2 . Take Three Values From User and Find the Greatest Number From Them

v1 = int(input("Enter The First Value : "))
v2 = int(input("Enter The Second Value : "))
v3 = int(input("Enter The Third Value : "))

if v1 > (v2 and v3):
    print("V1 is Greatest Number")
elif v2 > (v1 and v3):
    print("V2 is Greatest Number")
else:
    print("V3 is Greatest Number")




