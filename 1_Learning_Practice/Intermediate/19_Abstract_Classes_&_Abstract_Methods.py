# Python By Default Does not Support Abstract Classes or Methods
# We need to import "abc" module to make a class Abstract

# A Class Will be Called as An Abstract iff atleast one of the Methods of it Abstract


from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("i5")


# com = Computer()
com1 = Laptop()
# com.process()
com1.process()
