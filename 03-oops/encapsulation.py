# Encapsulation hides internal data and exposes a controlled interface.
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = Account(1000)
account.deposit(250)
print(account.get_balance())
