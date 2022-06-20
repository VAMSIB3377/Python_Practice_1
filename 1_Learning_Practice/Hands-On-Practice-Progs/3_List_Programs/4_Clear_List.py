lst = [4, 7, 9, 5, 6, 3, 5]

print(lst)
# lst.clear()
# lst = []
# del lst[:]

for i in range(len(lst)):
    lst.remove(lst[0])

print(lst)