class Bank:
    def __init__(self):
        self.__customers = []

    def createAccount(self):
        name = input("Enter Name: ")
        pin = input("Enter PIN: ")
        balance = float(input("Enter Initial Balance: "))

        customer = {
            "name": name,
            "pin": pin,
            "balance": balance
        }

        self.__customers.append(customer)
        print("Account Created Successfully!")

    def deposit(self):
        name = input("Enter Name: ")
        pin = input("Enter PIN: ")

        for customer in self.__customers:
            if customer["name"] == name and customer["pin"] == pin:
                amount = float(input("Enter Deposit Amount: "))
                customer["balance"] += amount
                print("Deposit Successful")
                return

        print("Invalid Name or PIN")

    def withdraw(self):
        name = input("Enter Name: ")
        pin = input("Enter PIN: ")

        for customer in self.__customers:
            if customer["name"] == name and customer["pin"] == pin:
                amount = float(input("Enter Withdrawal Amount: "))

                if amount <= customer["balance"]:
                    customer["balance"] -= amount
                    print("Withdrawal Successful")
                else:
                    print("Insufficient Balance")
                return

        print("Invalid Name or PIN")

    def checkBalance(self):
        name = input("Enter Name: ")
        pin = input("Enter PIN: ")

        for customer in self.__customers:
            if customer["name"] == name and customer["pin"] == pin:
                print("Current Balance:", customer["balance"])
                return

        print("Invalid Name or PIN")

    def displayCustomers(self):
        print("Customer Details")
        for customer in self.__customers:
            print("-----------------------")
            print("Name:", customer["name"])
            print("Balance:", customer["balance"])


bank = Bank()

while True:
    print("===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Customers")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        bank.createAccount()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.checkBalance()

    elif choice == "5":
        bank.displayCustomers()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")