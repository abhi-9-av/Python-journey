"""Practice 1: Create a class and an object.

Create a `Book` class with a method named `describe` that prints the book's
title and author. Create one Book object and call its method.

For this first exercise, set the title and author on the object after creating
it. Do not use a constructor yet.
"""


class Book:
    def describe(self):
        print(f"Title: {self.title}, Author:{self.author}")

book1 = Book()
book1.title=input("Enter title")
book1.author=input("Enter the author")

book1.describe()