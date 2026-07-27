from abc import *
class BankAccount(ABC):
    @abstractmethod
    def deposite(self, acc,amount):
        pass

    @abstractmethod
    def withdraw(self, acc,amount):
        pass
    
    @abstractmethod
    def display_balance(self):
        pass

class SavingAcc(BankAccount):
    def __init__(self, name,accno,balance=500):
        self.name=name
        self.accno=accno
        self.balance=balance

    def withdraw(self, acc,amount):
        if acc==self.accno:
            if amount>0:
                if amount<=self.balance:
                    print('Withdraw Successful')
                    self.balance -= amount
                else:
                    print('Insufficient Funds!!')
            else:
                print('Withdraw not possible for negative amount..') 
        else:
             print('Invalid account number')
    
    def deposite(self, acc,amount):
        if acc==self.accno:
            if amount>0:
                    print('Deposite Successful')
                    self.balance += amount
            else:
                print('Deposite not possible for negative amount..') 
        else:
             print('Invalid account number')
    
    def display_balance(self):
        return self.balance

class CurrentAccount(BankAccount):
    def __init__(self, name,accno,balance=0):
        self.name=name
        self.accno=accno
        self.balance=balance

    def withdraw(self, acc,amount):
        if acc==self.accno:
            if self.balance - amount >= -5000:
                    print('Withdraw Successful')
                    self.balance -= amount

                    if self.balance<0:
                         print("You are using overdraft facilities...")
            else:
                print('Insufficient Funds!!')
        else:
             print('Invalid account number')
    
    def deposite(self, acc,amount):
        if acc==self.accno:
            if amount>0:
                    print('Deposite Successful')
                    self.balance += amount
            else:
                print('Deposite not possible for negative amount..') 
        else:
             print('Invalid account number')
    
    def display_balance(self):
        return self.balance

savingcustomers=[SavingAcc("Rijan",12345),SavingAcc("Pappu",13579,1000),SavingAcc("Subodh",24684,1200),SavingAcc("Richa",54321,1500)]

print("Saving account Balance Details..")
for customer in savingcustomers:
    print(f'{customer.name} {customer.display_balance()}')
    print('--'*30)

print()
print("Current account  Details..")
currentcustomers=CurrentAccount("Lbef",12345,5000)
currentcustomers.withdraw(12345,8000)
print(f'Actual balance: {currentcustomers.display_balance()}')