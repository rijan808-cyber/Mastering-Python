class Bank:
    bank_name='Lbef Bank'
    def __init__(self, name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    
    def display(self):
        print(f'Bank Name: {self.bank_name}')
        print(f'Account holder: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: {self.balance}')
        print('--'*50)
        print()
    
    def deposite(self,acc, amount):
        if self.account_number == acc:
            self.balance = self.balance + amount
            print(f'{amount} is deposited sucessfully.')
        else:
            print('Invalid account number!! please enter valid account number')

    def withdraw(self,acc,amount):
        if self.account_number == acc:
            if self.balance>=amount:
                self.balance = self.balance - amount
                print(f'{amount} is withdrawn sucessfully.')
            else: 
                print(f'Insufficient balance..')
        else:
            print('Invalid account number!! please enter valid account number')

pappu=Bank("Pappu Gupta",12345,5000)
subodh=Bank("Subodh Acharaya",54321)
pappu.display()
subodh.display()
subodh.deposite(54321,5000)
subodh.withdraw(54321,3000)
subodh.display()