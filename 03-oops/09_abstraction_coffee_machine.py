"""Practice 9: Abstraction as a simple interface.

Create a `CoffeeMachine` class with a public method `make_coffee()` that
prints a simple result such as "Coffee is ready". Put the preparation steps
(for example, heating water and brewing coffee) in separate helper methods
whose names begin with an underscore. `make_coffee()` should call those
helpers in order. From outside the class, use only `make_coffee()`.

In a comment, explain which method is the simple interface and which details
are hidden from the person using the machine.
"""


class CoffeeMachine:

    def __heating_water(self):
        print("Water is being boiled")

    def __brewing_coffee(self):
        print("Coffee is being brewed")

    def __pouring(self):
        print("Your coffee is being served")
   
    def make_coffee(self):
        self.__heating_water()
        self.__brewing_coffee()
        self.__pouring()
        print("Your coffee is ready!")
waitor = CoffeeMachine()
waitor.make_coffee()