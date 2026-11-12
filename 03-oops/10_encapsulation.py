"""Practice 10: Encapsulation.

Create a `Wallet` class that stores its balance in a private attribute.
Provide `add_money(amount)`, `spend_money(amount)`, and `show_balance()`
methods. Do not allow non-positive additions or spending more than the
available balance. Try valid and invalid operations and display the balance.
"""


class Wallet:
    def __init__(self,balance):
        self.__balance=balance

    def add_money(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Enter a valid amount")

    def spend_money(self,amount):
        if amount > self.__balance :
            print("Insufficient Balance")
        else:
             self.__balance -= amount

    def show_balance(self):
        print(self.__balance)

wal1= Wallet(10000)
wal1.add_money(-100)
wal1.add_money(10000)
wal1.show_balance()
wal1.spend_money(40000)
wal1.spend_money(4000)
wal1.show_balance()

