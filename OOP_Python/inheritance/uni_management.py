class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age.")

    def __str__(self):
        return (
            f"Name : {self.__name}\n"
            f"Age  : {self.__age}"
        )


class Student(Person):
    def __init__(self, name, age, roll_number, gpa):
        super().__init__(name, age)
        self.__roll_number = roll_number
        self.__gpa = gpa

    def get_roll_number(self):
        return self.__roll_number

    def get_gpa(self):
        return self.__gpa

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def set_gpa(self, gpa):
        if 0 <= gpa <= 4:
            self.__gpa = gpa
        else:
            print("Invalid GPA.")

    def __str__(self):
        return (
            super().__str__()
            + f"\nRoll Number : {self.__roll_number}"
            + f"\nGPA         : {self.__gpa}"
        )


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.__subject = subject
        self.__salary = salary

    def get_subject(self):
        return self.__subject

    def get_salary(self):
        return self.__salary

    def set_subject(self, subject):
        self.__subject = subject

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary.")

    def __str__(self):
        return (
            super().__str__()
            + f"\nSubject     : {self.__subject}"
            + f"\nSalary      : Rs.{self.__salary}"
        )

student1 = Student(
    "Rijan Pariyar",
    21,
    "ST101",
    3.85
)

teacher1 = Teacher(
    "Om Prakash Panjiyar",
    35,
    "Python Programming",
    80000
)

print("Student Details")
print(student1)

print("\n-----------------------------\n")

print("Teacher Details")
print(teacher1)

student1.set_gpa(3.95)

teacher1.set_salary(90000)

print("\nAfter Updating Details\n")

print(student1)
print()
print(teacher1)