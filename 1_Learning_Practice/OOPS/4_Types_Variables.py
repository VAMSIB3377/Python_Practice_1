# 1. Instance Variables         --> If we define a Variable inside init then it will become an Instance Variable.
# 2. Class or Static Variables  --> If we define a Variable Outside the init then it is Class or Static Variable.
#                                   Class Variables Can be Called Using Class Name.

class Car:

    wheels = 4     # Class Variable

    def __init__(self):
        self.mil = 10  # Instance Variable
        self.com = "BMW"  # Instance Variable


c1 = Car()
c2 = Car()

c1.mil = 50
Car.wheels = 6

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
