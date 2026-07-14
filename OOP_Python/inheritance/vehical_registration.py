class Vehicle:
    def __init__(self, registration_number, brand):
        self.__registration_number = registration_number
        self.__brand = brand

    def get_registration_number(self):
        return self.__registration_number

    def get_brand(self):
        return self.__brand

    def set_registration_number(self, registration_number):
        self.__registration_number = registration_number

    def set_brand(self, brand):
        self.__brand = brand

    def __str__(self):
        return (
            f"Registration Number : {self.__registration_number}\n"
            f"Brand               : {self.__brand}"
        )


class Car(Vehicle):
    def __init__(self, registration_number, brand, model, price):
        super().__init__(registration_number, brand)
        self.__model = model
        self.__price = price

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Invalid price!")

    def __str__(self):
        return (
            super().__str__()
            + f"\nModel               : {self.__model}"
            + f"\nPrice               : Rs.{self.__price}"
        )


class ElectricCar(Car):
    def __init__(self, registration_number, brand, model, price, battery_capacity, charging_time):
        super().__init__(registration_number, brand, model, price)
        self.__battery_capacity = battery_capacity
        self.__charging_time = charging_time

    def get_battery_capacity(self):
        return self.__battery_capacity

    def get_charging_time(self):
        return self.__charging_time

    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def set_charging_time(self, charging_time):
        self.__charging_time = charging_time

    def __str__(self):
        return (
            super().__str__()
            + f"\nBattery Capacity    : {self.__battery_capacity} kWh"
            + f"\nCharging Time       : {self.__charging_time} hours"
        )


car1 = ElectricCar(
    "BA-01-PA-1234",
    "Tesla",
    "Model 3",
    6500000,
    75,
    8
)

print("Electric Car Details")
print(car1)

car1.set_price(6200000)
car1.set_battery_capacity(82)
car1.set_charging_time(7)

print("\nAfter Updating Details")
print(car1)