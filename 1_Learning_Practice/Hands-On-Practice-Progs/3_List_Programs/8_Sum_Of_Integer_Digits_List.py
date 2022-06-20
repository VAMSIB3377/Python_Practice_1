lst = [34, 'abc',  {8, 6, 4, 7}, 67, (7, 6, 8, 6, 5), 26, 52]
x = 0

for i in lst:
    if type(i) == int:
        x = x + i


print(x)