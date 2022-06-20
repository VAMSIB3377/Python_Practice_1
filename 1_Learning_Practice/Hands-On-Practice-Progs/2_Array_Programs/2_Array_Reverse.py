# Reversal of an Array
import numpy
from numpy import array

arr = array([5, 6, 8, 7, 6, 4])

# a = numpy.flip(arr)
# print(a)

a = arr[::-1]
print(a)

4
5
6
7
8
9
10
11
12
13
# Example input list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def Reverse(numbers):
    if (len(numbers) == 1):
        return numbers
    return Reverse(numbers[1:]) + numbers[0:1]


# Test function
print(Reverse(numbers))


