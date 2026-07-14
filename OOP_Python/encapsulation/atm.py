class ATM:
    def __init__(self, name, pin, balance):
        self.__name = name
        self.__pin = pin
        self.__balance = balance

    def checkPin(self, pin):
        return self.__pin == pin

    def checkBalance(self, pin):
        if self.checkPin(pin):
            print("Current Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def deposit(self, pin, amount):
        if self.checkPin(pin):
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if self.checkPin(pin):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")

    def changePin(self, old_pin, new_pin):
        if self.checkPin(old_pin):
            self.__pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Incorrect Old PIN")

    def displayInfo(self):
        print("Account Information")
        print("Customer Name :", self.__name)
        print("Balance       :", self.__balance)

atm = ATM("Rijan", 1234, 10000)

atm.checkBalance(1234)

atm.deposit(1234, 5000)

atm.withdraw(1234, 3000)

atm.changePin(1234, 4321)

atm.checkBalance(4321)

atm.displayInfo()