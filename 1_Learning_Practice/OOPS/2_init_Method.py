class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        return self.cpu, self.ram


com1 = Computer('i5', '16GB')
print(com1.config())
