class Student:
    def __init__(self, name, roll, m1, m2, m3, m4, m5):
        self.name = name
        self.roll = roll
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 80:
            print("Grade: A")
        elif p >= 60:
            print("Grade: B")
        elif p >= 50:
            print("Grade: C")
        else:
            print("Grade: F")

student = Student("Rijan", 1, 80, 70, 90, 85, 75)

print("Total =", student.total())
print("Percentage =", student.percentage())

student.grade()