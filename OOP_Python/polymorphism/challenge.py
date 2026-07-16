class Payment:

    def pay(self, amount):
        print("Processing payment of", amount)


class CreditCard(Payment):

    def pay(self, amount):
        super().pay(amount)
        print("Paid using Credit Card")


class DebitCard(Payment):

    def pay(self, amount):
        super().pay(amount)
        print("Paid using Debit Card")


class UPI(Payment):

    def pay(self, amount):
        super().pay(amount)
        print("Paid using UPI")


class PayPal(Payment):

    def pay(self, amount):
        super().pay(amount)
        print("Paid using PayPal")

class Cash:

    def pay(self, amount):
        print("Paid", amount, "using Cash")


class Wallet:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


payments = [
    CreditCard(),
    DebitCard(),
    UPI(),
    PayPal(),
    Cash()
]

for payment in payments:
    payment.pay(1000)
    print("----------------")


wallet1 = Wallet(5000)
wallet2 = Wallet(3500)

print("Combined Wallet Balance =", wallet1 + wallet2)