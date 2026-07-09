class Human:
    college = 'LBEF' 
    def __init__(self):
        self.name = "LBEF"
        self.size = 27
        self.color = "White"   

    def display(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"College: {Human.college}")

h1=Human()
h2=Human()

h1.display()
print()
h2.display()