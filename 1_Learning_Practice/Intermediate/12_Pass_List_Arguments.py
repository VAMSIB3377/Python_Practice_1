def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [47, 89, 8, 45, 37, 68]
even, odd = count(lst)

print("Even : {} \nOdd : {}".format(even, odd))
print("\n\n")


# Assignment

# 1. Take 10 Names from the User And Count The Names
#    Which has a Length of more than 5.

def names_len(x):
    a_n = []
    for i in range(len(x)):
        if len(x[i]) > 5:
            a_n.append(x[i])
    return a_n

names = []
for i in range(1, 11):
    n = input("Enter the {} Name : ".format(i))
    names.append(n)

print(names_len(names))
