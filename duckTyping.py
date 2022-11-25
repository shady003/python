class human:
    def info(self, name):
        print('Name : {} Current Age : {}'.format(name.name, name.age))

class male:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        # self.name = self

h1 = human()

Saurabh = male('Saurabh', 22)
Sunder_pichai = male('Sunder', 50)
h1.info(Saurabh)
h1.info(Sunder_pichai)
