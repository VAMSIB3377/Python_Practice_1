# Binary Search - It is a Divide and Conquer Algorithm
#                 In Case of Binary Search It is Necessary That the Values Must Be Sorted.
#                 In Binary Search We will Divide the List into 2 parts Using Low Index and High Index (Low + High // 2)
#                 We will Compare the Elements with the Element that we need to Search
#                 If the Value of the Search Element is Less than the Middle Element we will make the index of
#                 Middle Element as High or If The Value of the Search Element is Higher than the Middle Element
#                 then the Index of the Middle Element Will Become Low.
#                 This Process Continues Until we Find the Element we Required.

# def Binary_Search(lst, low, high, mid, s):
#       if lst[mid] == s:
#          return "{} Found at Index: {}".format(s, mid)
#       elif s < lst[mid]:
#            low = 0
#            high = mid
#            mid = (low + high) // 2
#            return Binary_Search(lst, low, high, mid, s)
#        elif s > lst[mid]:
#            low = mid
#            high = len(lst)
#            mid = (low + high) // 2
#            return Binary_Search(lst, low, high, mid, s)
#        else:
#            return "{} is Not Found in The List"


lst = [8, 37, 4, 64, 98, 5, 44]
lst.sort()
print(lst)
# low = 0
# high = len(lst)
# mid = (low + high) // 2
s = 77
# print(Binary_Search(lst, low, high, mid, s))

pos = -1

def Binary_Search_1(lst,s):
    l = 0
    u = len(lst)-1
    while l <= u:
        mid = (l+u)//2
        if lst[mid] == s:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < s:
                l = mid+1
            else:
                u = mid-1
    return False


if Binary_Search_1(lst, s):
    print("Found at Index : ", pos)
else:
    print("{} is Not Found".format(s))
