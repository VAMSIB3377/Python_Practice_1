# Method Overloading - Multiple Methods in Having Same Name and Different No.of Parameteres and
#                      Different Types of Parameters is known as Method Overloading

# There is no such thing called as Method Overloading in Python
# In Python we may Overload Methods but can only use the latest Defined Methods


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        x = 0
        if a != None and b!=None and c!=None:
            x = a+b+c
        elif a != None and b!=None:
            x = a+b
        else:
            x = a
        return x


s1 = Student(56, 78)


print(s1.sum(5, 20, 10))
