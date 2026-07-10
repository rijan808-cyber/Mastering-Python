class Book:
    def __init__(self, id, name, author, price):
        self.id = id
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.id)
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)

    def updatePrice(self, newPrice):
        self.price = newPrice

    def discount(self):
        self.price = self.price - (self.price * 10 / 100)

book = Book(1, "Python", "John", 1000)

book.display()

book.updatePrice(1200)
book.discount()

print("After Discount")
book.display()