# RIZKY ANANTA FADHILA / 21120122120029
# SANDRO C. RAJAGUKGUK / 21120122130083
# BAYU ADRIYANTO  SOEPADMO /21120122140165
# I MADE SURYANATHA BHASKARA / 21120122140126
# SHIFT : 2
# KELOMPOK : 12

from abc import  ABC, abstractmethod

class Vehicle(ABC):

    model = None
    year = None
    color = None

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def __init__(self,model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " "  + self.model + " is stopped")

class Motorcycle(Vehicle):

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

class Truck(Vehicle):

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

car = Car("Corvette", 2021, "blue")
print("Car Model : " + car.getModel())
print("Year : " + str(car.year))
print("Color : " + car.color)
car.go()
car.stop()
print("---------------------------------------")
motorcycle = Motorcycle("Ducati", 2020, "grey")
print("Motorcycle Model : " + motorcycle.getModel())
print("Year : " + str(motorcycle.year))
print("Color : " + motorcycle.color)
motorcycle.go()
motorcycle.stop()
print("---------------------------------------")
truck = Truck ("Volvo", 2019, "black")
print("Truck Model : " + truck.getModel())
print("Year : " + str(truck.year))
print("Color : " + truck.color)
truck.go()
truck.stop()
