class Computer:

    def __init__(self, cpu, ram):   # Constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):

        print(self.cpu, self.ram)


com1 = Computer('i5', 6)
com2 = Computer('Ryzon 5',16)
Computer.config(com1)
com2.config()

a = 100
print(a.bit_length())
