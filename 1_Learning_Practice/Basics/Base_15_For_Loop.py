"""
n = "VAMSI"

for i in n:
    print(i)


for i in (7,43,6,6,"VAMSI"):    # List of Sequence Values
    print(i)


for i in range(1, 11):
    print(i, end=" ")


for i in range(20, 5, -1):
    print(i, end=" ")



for i in range(1, 21):
    if i%5 != 0:
        print(i)

"""

# Assignment

# 1. Print All The Perfect Square Numbers Between 1 and 50

for i in range(1, 51):
    if i**( 0.5 ) == int(i**( 0.5 )):
        print(i, end=" ")