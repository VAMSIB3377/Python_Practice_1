# Polymorphism = poly + morph --> poly  - Many
#                             --> morph - Form

# Duck Typing - Duck typing is a concept related to dynamic typing,
#               where the type or the class of an object is less important than the methods it defines.
#               When you use duck typing, you do not check types at all.
#               Instead, you check for the presence of a given method or attribute.

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
