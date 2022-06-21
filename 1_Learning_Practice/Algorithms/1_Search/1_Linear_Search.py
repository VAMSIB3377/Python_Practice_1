# Linear Search - Comparing Every Item or Element in a List with The Element We Need to Find Until We Find it.

# Simple Search

# if 4 in lst:
#     print(lst.index(4))

pos = -1


def Linear_Search(l, a):
    # i = 0
    # while i < len(l):
    #     if l[i] == a:
    #         globals()['pos'] = i
    #         return True
    #     i = i+1
    # return False

    for i in range(len(l)):
        if l[i] == a:
            # globals()['pos'] = i
            # return True
            return "Found at index : {} ".format(i)

    else:
        return "Not Found"


lst = [5, 8, 4, 6, 9, 2]
n = 6

"""
if Linear_Search(lst, n):
    print("Found at : ", pos)
else:
    print("Not Found")
    
"""
print(Linear_Search(lst, n))
