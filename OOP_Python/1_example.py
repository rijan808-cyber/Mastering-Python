class Human:
    color = "Brown"
    name = "Rijan Pariyar"
    size = 5
    hand = 2
    leg = 2

    def walk(self):
        print("Human is Walking...")
    def sleep(self):
        print("Human is Sleeping...")
    def eat(self):
        print("Human is Eating...")

h1=Human()
print(f"Name: {h1.name}")
print(f"Size: {h1.size}")
h1.eat()