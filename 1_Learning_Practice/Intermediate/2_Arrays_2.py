from array import *
"""
arr = array('i', [])

n = int(input("Enter the length of the Array : "))
for i in range(n):
    x = int(input("Enter the Next Value : "))
    arr.append(x)


print(arr)


val = int(input("Enter the Value for Search : "))
for i in range(1, len(arr)):
    if val == arr[i]:
        print("Value Found at Index : ", i)
"""

# Assignments

# 1. Ceate an array With 5 Values and delete
#    the value at index number 2 without using inbuilt funtion

arr1 = array('i', [7, 8, 4, 6, 9])
ind = int(input("Enter the index Number of The Number That You Want to Delete : "))
"""
c = [ e for i,e in enumerate(arr1) if i != ind ]
print(arr1)
print(c)

"""

arr1 = arr1[0:ind]+arr1[ind+1:]
print(arr1)

# 2. Write a code to reverse an array without using
#    in-built function

rev = arr1[::-1]
print(rev)

for i in range(int(len(arr1)/2)):
    n = arr1[i]
    arr1[i] = arr1[len(arr1)-i-1]
    arr1[len(arr1) - i - 1] = n

print(arr1)
