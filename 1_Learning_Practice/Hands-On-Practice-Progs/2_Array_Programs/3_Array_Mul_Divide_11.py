from numpy import array
a = array([100, 10, 5, 25, 35, 14])
n = 11
x = 1
for i in range(len(a)):
    x = a[i]*x

d = x % 11
print(d)