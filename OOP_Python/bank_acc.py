class BankAccount:
    def __init__(self, accNo, name, balance):
        self.accNo = accNo
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Balance =", self.balance)

acc = BankAccount(1001, "Rijan", 10000)

acc.deposit(5000)
acc.withdraw(3000)

acc.display()