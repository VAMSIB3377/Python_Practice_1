a = 10
print(id(a))

def something():

    a = 9

    x = globals()['a']
    print(id(x))
    print("Inside the Function : ", a)

    globals()['a'] = 15
    print(id(a))



something()
print("Outside The Function : ", a)

