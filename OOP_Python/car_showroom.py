class Car:
    def __init__(self, brand, model, price, fuel):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = fuel

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel:", self.fuel)

    def affordable(self):
        if self.price < 3000000:
            print("Affordable")
        else:
            print("Not Affordable")

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

car = Car("Hyundai", "i20", 2800000, "Petrol")

car.display()

car.affordable()

car.discount(10)

print("After Discount")
car.display()