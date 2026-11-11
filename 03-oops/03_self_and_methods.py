"""Practice 3: Use self in an instance method.

Create a `Dog` class whose constructor stores a name. Add a `bark` method that
prints "<name> says woof!". Make two dogs and call bark on each one.
"""


class Dog():
    def __init__(self):
        self.name=input("Enter the name")
    def bark(self):
        print(f"{self.name} says woof!")

tommy= Dog()
bruno= Dog()
tommy.bark()
bruno.bark()