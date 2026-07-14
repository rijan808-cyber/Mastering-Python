class Bank:
   # bank_name='Lbef Bank'
    def __init__(self, name,account_number,balance=0):
        self.__name=name
        self.__account_number=account_number
        self.__balance=balance
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name
    
    def getAccount(self):
        return self.__account_number
    
    def setAccount(self, acc):
        self.__account_number=acc
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self,amount):
        self.__balance=amount
    
    def display(self):
        #print(f'Bank Name: {self.bank_name}')
        print(f'Account holder: {self.__name}')
        print(f'Account Number: {self.__account_number}')
        print(f'Current Balance: {self.__balance}')
        print('--'*50)
        print()
    
    def deposite(self,acc, amount):
        if self.__account_number == acc:
            self.__balance = self.__balance + amount
            print(f'{amount} is deposited sucessfully.')
        else:
            print('Invalid account number!! please enter valid account number')

    def withdraw(self,acc,amount):
        if self.__account_number == acc:
            if self.__balance>=amount:
                self.__balance = self.__balance - amount
                print(f'{amount} is withdrawn sucessfully.')
            else: 
                print(f'Insufficient balance..')
        else:
            print('Invalid account number!! please enter valid account number')

i=1
customers=[]
while True:
    print()
    name=input(f'Enter Customer{i} name: ')
    acc=int(input(f'Enter customer{i} account number: '))
    balance=float(input(f'Enter Customer{i} initial balance: '))
    c=Bank(name,acc,balance)
    customers.append(c)
    i+=1
    
    option=input('Doy you want more? [yes/no]: ')
    if option.lower()=='no':
        break

for customer in customers:
    print(customer.display())

