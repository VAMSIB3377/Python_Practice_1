lst = [93, 84, 57, 13, 66, 45]

n = int(input("Enter the no.of Largest Numbers You Need : "))

lst.sort()
lst.reverse()

for i in range(1, n+1):
    print(lst[i])
