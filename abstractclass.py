from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):              # medatorymethod
        print('Process from laptop')


class Whiteboard():
    def write(self):
        print('its writing')


class Programmer:
    def work(self, com):
        print('Soling Bugs')
        com.write()

# c0 = Computer()
c1 = Laptop()
w1 = Whiteboard()
p1 = Programmer()
c1.process()
p1.write(w1)
