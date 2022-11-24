# Sum of Array

from numpy import array

a = array([6, 15, 4, 7, 9, 2])
x = 0
for i in range(len(a)):
    x = a[i] + x
print(x)

# Largest Element in an Array
# print(max(a))
m = 0
for i in range(len(a) - 1):
    if a[i] > m:
        m = a[i]

print(m)

