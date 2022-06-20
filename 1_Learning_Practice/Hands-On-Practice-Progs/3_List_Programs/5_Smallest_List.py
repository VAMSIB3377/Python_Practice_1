lst = [4, 7, 9, 5, 1, 6, 3]

s = 100000

for i in range(len(lst)):
    if lst[i] < s:
        s = lst[i]
print(s)
