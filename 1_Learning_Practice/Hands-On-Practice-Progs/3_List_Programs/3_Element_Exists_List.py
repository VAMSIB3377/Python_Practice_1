lst = [4, 7, 9, 5, 6, 3, 5]
element = int(input("Enter the element that you want to Find : "))

for i in range(0, len(lst)):
    if lst[i] == element:
        print("{} is there in the List at index {}".format(element, i))
        break

