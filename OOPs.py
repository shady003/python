class Computer:
    director = 'Saurabh_yadav'
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):

        print(self.cpu, self.ram)
    def dir(self):
        return self.director

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
r = 22/7
print('{:.2f}'.format(r))
print(Computer.dir(com1))
# @staticmethod
# @classmethod