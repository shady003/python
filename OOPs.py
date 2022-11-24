class Computer:

    def config(self):

        print('i5, 16gb, 1TB')


com1 = Computer()
com2 = Computer()
Computer.config(com1)
com2.config()

a = 100
print(a.bit_length())
