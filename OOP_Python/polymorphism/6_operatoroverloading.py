class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    
    def __add__(self,other):
        return self.marks + other.marks
    
    def __gt__(self,other):
        if self.marks>other.marks:
            return True
        else:
            False

s1=Student("Rijan",55)
s2=Student("Sanjay",40)
print(s1+s2)
print(s1>s2)