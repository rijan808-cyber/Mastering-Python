class Human:
    college = 'LBEF' # Class Variable
    def __init__(self, name, size, color): # name, size, color(local variable)
        self.name = name
        self.size = size                   # name, size, color(Instance variable)
        self.color = color   

    def display(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"College: {Human.college}")

h1=Human("Pappu Gupta", 5,"Black & white")
h2=Human("Ramu Bohara", 4,"Complexion")      # h1, h2, h3 (Reference variable) 
h3=Human("Ajay Bahadur Shrestha",6,"Gora Chitta")

h1.display()
print()
h2.display()
print()
h3.display()