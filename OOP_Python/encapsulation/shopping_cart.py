class ShoppingCart:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__total_amount = 0

    def getTotal(self):
        return self.__total_amount

    def setCustomerName(self, name):
        self.__customer_name = name

    def addItem(self, price):
        self.__total_amount += price
        print("Item added.")

    def removeItem(self, price):
        if self.__total_amount - price >= 0:
            self.__total_amount -= price
            print("Item removed.")
        else:
            print("Total amount cannot be negative.")

    def displayBill(self):
        print("\nCustomer Name :", self.__customer_name)
        print("Total Amount  :", self.__total_amount)


cart = ShoppingCart("Rijan")

cart.addItem(500)
cart.addItem(1000)

cart.displayBill()

cart.removeItem(300)

cart.displayBill()

cart.removeItem(5000)