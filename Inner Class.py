class Car:
    def __init__(self, name, milege, model, cc):
        self.name = name
        self.milege = milege
        self.inf = self.info(model, cc)

    class info:
        def __init__(self, model, cc):
            self.model = model
            self.cc = cc


        def getmodel(self):
            return self.model


magnite = Car('nissan', 18, 'magnite', 999)
print(magnite.inf.model)
mag=Car.info('Name',99)
print(mag.model)