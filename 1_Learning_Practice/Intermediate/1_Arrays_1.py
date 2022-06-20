"""
from array import *

vals = array('i', [8, 7, 6, 4, 3, 5])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
print(vals.index(6))
vals.remove(4)
print(vals)
vals.reverse()
print(vals)

for i in range(len(vals)):
    print(vals[i], end=" ")

print("\n\n")

vals_1 = array('u', ['a', 'e', 'i', 'o', 'u'])
print(vals_1)
for i in vals_1:
    print(i, end=" ")

print("\n\n")

# When we don't know the type
arr = array(vals.typecode, (a*2 for a in vals))
for i in arr:
    print(i, end=" ")

"""


# Assignments

# 1. Write a Code to sort the array in ascending order

from array import *

nums = array('i', [8, 4, 7, 3, 5, 2])

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
