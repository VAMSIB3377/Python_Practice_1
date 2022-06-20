class Computer:

    def __init__(self):
        self.name = "Vamsi"
        self.age = 25

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False




c1 = Computer()
c2 = Computer()



c1.age = 22
c1.name = "abc"

c2.update()

if c1.compare(c2):
    print("They are same")

print(c1.name, c1.age)
print(c2.name, c2.age)
