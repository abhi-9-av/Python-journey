"""Practice 12: Bank account mini project.

Create a `BankAccount` class with an account holder and a private balance.
Add methods to credit (deposit) an amount, debit (withdraw) an amount, and
check the balance. Reject non-positive transactions and debits larger than
the available balance. Create two accounts and demonstrate valid and invalid
transactions, then check each balance.
"""



class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def credit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Enter a valid amount")

    def debit(self,amount):
        if amount > self.__balance :
            print("Insufficient Balance")
        elif amount<0:
            print("Enter a valid amount")
        else:
             self.__balance -= amount

    def show_balance(self):
        print(self.__balance)

wal1= BankAccount(10000)
wal1.credit(-100)
wal1.credit(10000)
wal1.show_balance()
wal1.debit(40000)
wal1.debit(4000)
wal1.show_balance()

wal2= BankAccount(20000)
wal2.credit(-1000)
wal2.credit(10000)
wal2.show_balance()
wal2.debit(40000)
wal2.debit(4000)
wal2.show_balance()

