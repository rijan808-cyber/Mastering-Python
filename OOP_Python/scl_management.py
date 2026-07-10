class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience)

    def senior(self):
        if self.experience >= 10:
            print("Senior Teacher")
        else:
            print("Junior Teacher")

    def promotion(self):
        self.experience += 1


teachers = [
    Teacher("Ram", "Math", 12),
    Teacher("Sita", "Science", 8),
    Teacher("Hari", "English", 15)
]

for t in teachers:
    print()
    t.display()
    t.senior()
    t.promotion()

print("After Promotion")

for t in teachers:
    print()
    t.display()