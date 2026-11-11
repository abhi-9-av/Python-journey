"""Practice 5: Build an object from several pieces of data.

Create a `Person` class with a constructor that stores a name and age. Add an
`introduce` method that prints: "Hi, I'm <name> and I'm <age> years old.".
Create a person and call introduce().
"""


class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hi I'm {self.name} and I'm {self.age} years old.")

human = Person("Abhinav", 18)
human.introduce()
