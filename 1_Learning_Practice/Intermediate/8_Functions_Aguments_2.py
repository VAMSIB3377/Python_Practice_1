def update(x):
    x = 8
    print("x ", x)


a = 10
update(a)
print("a ", a)
print("\n\n")


def update_lst(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("x ", lst)


lst = [10, 20, 30]
print(id(lst))
update_lst(lst)
print("lst ", lst)
