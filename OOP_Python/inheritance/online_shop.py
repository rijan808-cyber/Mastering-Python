class Product:
    def __init__(self, product_id, product_name, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Invalid Price!")

    def calculate_price(self):
        return self.__price

    def __str__(self):
        return (
            f"Product ID   : {self.__product_id}\n"
            f"Product Name : {self.__product_name}\n"
            f"Price        : Rs.{self.__price}"
        )


class DiscountProduct(Product):
    def __init__(self, product_id, product_name, price, discount):
        super().__init__(product_id, product_name, price)
        self.__discount = discount

    def get_discount(self):
        return self.__discount

    def set_discount(self, discount):
        if 0 <= discount <= 100:
            self.__discount = discount
        else:
            print("Invalid Discount!")

    def calculate_price(self):
        original_price = super().calculate_price()
        final_price = original_price - (original_price * self.__discount / 100)
        return final_price

    def __str__(self):
        return (
            super().__str__()
            + f"\nDiscount    : {self.__discount}%"
            + f"\nFinal Price : Rs.{self.calculate_price():.2f}"
        )

product1 = DiscountProduct(
    "P101",
    "Gaming Laptop",
    120000,
    15
)

print("Product Details")
print(product1)

product1.set_price(130000)
product1.set_discount(20)

print("\nAfter Updating Details")
print(product1)