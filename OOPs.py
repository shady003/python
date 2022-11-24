class Computer:
    director = 'Saurabh'
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    # @classmethod
    def config(self):

        print(self.cpu, self.ram)


com1 = Computer('i5', 6)  # Constructor
com2 = Computer('Ryzon 5',16)  # Constructor
com1.ram = 16
Computer.config(com1)
com2.config()
print(com1.director)

print(id(com1))
print(id(com2))
a = 100
print(a.bit_length())
