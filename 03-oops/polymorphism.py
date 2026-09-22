# Polymorphism means the same method name can behave differently.
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.sound())
