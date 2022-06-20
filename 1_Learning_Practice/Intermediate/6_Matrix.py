
from numpy import *

arr1 = array([
                [1, 2, 3, 4, 8, 6],
                [9, 8, 7, 6, 3, 5]
            ])

"""
print(arr1.dtype)
print(arr1.ndim)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)
arr3 = arr2.reshape(3, 4)
print(arr3)
arr4 = arr2.reshape(2, 2, 3)
print(arr4)
"""

m1 = matrix('1 2 3 ; 4 5 7 ; 6 7 8')
m2 = matrix('6 5 4 ; 6 3 2 ; 1 5 3')

m3 = m1 + m2
m4 = m1 * m2
print(m3)
print("\n\n")
print(m4)
print("\n\n")
print(m1)
print("\n\n")
print(diagonal(m1))
print("\n\n")
print(m1.max())
