# In Any Sorting Technique Swapping is one the Concept Which is Necessary to Use.

# Bubble Sort - In Bubble Sort We Will Compare Each and Every Element With the Next Element.
#               So, We Iterate The Loop until The Before Element of the Last Element.
#               By Using Only one Loop we will Iterate the List Only One
#               So, We will use Another Loop to iterate the
#               Inner Loop Which will Give n-1 no.of Iterations where 'n' is the Length of the List


def Bubble_Sort(lst):
    """
    Not Bubble Sort

    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)
    return lst
    """

    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lst = [27, 3, 5, 42, 77, 9]

print(Bubble_Sort(lst))
