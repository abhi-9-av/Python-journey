# Inheritance allows a child class to use features from a parent class.
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

pet = Dog()
print(pet.speak())
print(pet.bark())
