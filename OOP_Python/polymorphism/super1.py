class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)


c1 = Car("Toyota", "Corolla", "Petrol")
c1.display()