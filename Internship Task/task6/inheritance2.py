"""
We are designing a system that models different types of vehicles. The base class, Vehicle,
contains common attributes for all vehicles (like brand and model). The Car class inherits
from Vehicle and adds attributes specific to cars (like num_doors). Finally, the ElectricCar
class inherits from Car and adds features specific to electric cars (like battery_capacity).
"""

class Vechile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vechile):
    def __init__(self,brand,model,num_doors):
        super().__init__(brand,model)
        self.num_doors=num_doors
class ElectricCar(Car):
    def __init__(self,brand,model,num_doors,battery_capacity):
        super().__init__(brand,model,num_doors)
        self.battery_capacity=battery_capacity
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Num_doors:",self.num_doors)
        print("Battery_capacity:",self.battery_capacity)
e=ElectricCar('TATA','abc120',4,20000)
e.display()
