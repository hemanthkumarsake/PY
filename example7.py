class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getName(self):
        print(self.name)
    def getPrice(self):
        print(self.price)
p1=Product("Milk", 39)
p1.getName()
p1.getPrice()
p2=Product("Paneer", 100)
p2.getName()
p2.getPrice()