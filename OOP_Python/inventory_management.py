class Inventory:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def addStock(self, amount):
        self.quantity = self.quantity + amount

    def removeStock(self, amount):
        if amount <= self.quantity:
            self.quantity = self.quantity - amount
        else:
            print("Not Enough Stock")

    def value(self):
        return self.quantity * self.price

    def display(self):
        print("Product:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Value:", self.value())

        if self.quantity < 10:
            print("Low Stock")
        else:
            print("Stock Available")

item1 = Inventory(1, "Laptop", 5, 80000)
item2 = Inventory(2, "Mouse", 20, 800)

item1.addStock(5)
item2.removeStock(5)

item1.display()

print()

item2.display()