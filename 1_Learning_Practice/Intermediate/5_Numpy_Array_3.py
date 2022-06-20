# Shallow Copy --> Both the arrays will be dependent on each other so
#                  if we update the value in one array it reflects in the other array too

# Deep Copy --> The Two Different arrays which are not linked in any way in which one array
#               would be copied from other



from numpy import *
import itertools


"""
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([8, 9, 4, 2, 7])

arr3 = arr1 + arr2  # Vectorized Operation
print(sin(arr3))
print(cos(arr3))
print(tan(arr3))
print(min(arr3))
print(max(arr3))
print(sqrt(arr3))
print(sort(arr3))
print(sum(arr3))
print(concatenate([arr1, arr2]))

# Copying an array

print("\n\n")

arr4 = arr3    # Aliasing
print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))

print("\n\n")
arr4 = arr3.view()  # Shallow Copy
print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))


print("\n\n")
arr4 = arr3.copy()  # Deep Copy
print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))
"""






# Assignment
"""
for i in range(len(arr)):
    arr[i] = arr[i] + 5
print(arr)


arr = arr + 5
print(arr)

"""

# 1. Write a code to add 2 arrays using forloop.
"""
arr1 = array([2, 3, 4, 5, 6])
arr2 = array([8, 7, 6, 5, 4])
arr3 = array([0, 0, 0, 0, 0])

for i in range(len(arr1) | len(arr2)):
    arr3[i] = arr1[i]+arr2[i]
print(arr3)
"""

# 2. Write a code to find the maximum value from an array without using in built functions

arr = array([82, 97, 26, 115, 44])
h = 0
for num in arr:
    if num > h:
        h = num
print("The Hihgest Number is : ", h)

