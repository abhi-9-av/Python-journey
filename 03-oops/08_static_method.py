"""Practice 8: Static methods.

Create a `NumberTools` class with a static method `is_even(number)` that
returns True when the number is even and False otherwise. The method should
not use self or access object attributes. Call it through the class for a
couple of numbers and print the results.
"""

class NumberTools:
    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False
print(NumberTools.is_even(100))
print(NumberTools.is_even(178))
print(NumberTools.is_even(111))
print(NumberTools.is_even(109))
