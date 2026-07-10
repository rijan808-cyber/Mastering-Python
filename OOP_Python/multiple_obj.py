class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def display(self):
        print(self.id, self.name, self.price)

p1 = Product(1, "Laptop", 80000)
p2 = Product(2, "Mouse", 1000)
p3 = Product(3, "Keyboard", 3000)
p4 = Product(4, "Monitor", 25000)
p5 = Product(5, "Printer", 15000)

products = [p1, p2, p3, p4, p5]

print("All Products")

for p in products:
    p.display()

highest = p1
lowest = p1
total = 0

for p in products:
    total = total + p.price

    if p.price > highest.price:
        highest = p

    if p.price < lowest.price:
        lowest = p

print("Most Expensive:", highest.name)
print("Cheapest:", lowest.name)
print("Average Price:", total / 5)