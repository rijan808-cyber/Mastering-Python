class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_holder(self, name):
        self.__account_holder = name

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount}")
        else:
            print("Insufficient Balance")

    def __str__(self):
        return (
            f"Account Number : {self.__account_number}\n"
            f"Account Holder : {self.__account_holder}\n"
            f"Balance        : Rs.{self.__balance}"
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, rate):
        self.__interest_rate = rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate / 100
        self.deposit(interest)

    def __str__(self):
        return (
            super().__str__()
            + f"\nInterest Rate : {self.__interest_rate}%"
        )


account = SavingsAccount("ACC101", "Rijan Pariyar", 50000, 5)

print("Initial Details")
print(account)

print("\nAdding Interest...")
account.add_interest()

print("\nAfter Interest")
print(account)

print("\nDepositing Rs.5000")
account.deposit(5000)

print("\nWithdrawing Rs.10000")
account.withdraw(10000)

print("\nFinal Details")
print(account)