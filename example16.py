from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine")
class Fridge(Appliance):
    def turn_on(self):
        print("Fridge")
w=WashingMachine()
w.turn_on()
fridge=Fridge()
fridge.turn_on()