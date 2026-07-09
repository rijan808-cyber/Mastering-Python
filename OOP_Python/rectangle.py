class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

l=int(input("Enter Length of rectangle: "))
b=int(input("Enter Breadth of rectangle: "))
R1 = Rectangle(l,b)
print(f"Area of rectangle: {R1.area()}")
print(f"Perimeter of rectangle: {R1.perimeter()}")