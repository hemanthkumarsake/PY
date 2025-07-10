class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("Meow")
class Dog(Animal):
    def sound(self):
        print("Wow")
for s in [Cat(), Dog()]:
    s.sound()