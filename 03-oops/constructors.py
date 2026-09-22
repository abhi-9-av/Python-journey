# Constructors run automatically when a new object is created.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Meera", 500)
print(account.deposit(200))
