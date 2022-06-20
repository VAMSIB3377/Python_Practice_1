def Bubble_Sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)
    return lst


lst = [5, 3, 8, 6, 7, 2]

print(Bubble_Sort(lst))
