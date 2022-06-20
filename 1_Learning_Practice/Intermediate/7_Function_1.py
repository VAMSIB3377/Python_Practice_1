# Functions can be Called as Methods in Python
# Which are Used to Write the Reusable code.
# A Method Will Perform a Certain Task
# def is a keyword which used to create a method


def greet():
    print("Hello\nGood Morning")


def add(x, y):
    return x + y


def add_sub(x, y):
    return x + y, x - y


greet()
result = add(5, 4)
result1, result2 = add_sub(6, 3)
print(result)
print(result1, result2)
