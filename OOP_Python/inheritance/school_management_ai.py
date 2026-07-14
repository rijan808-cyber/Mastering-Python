class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

    def __str__(self):
        return (
            f"Name : {self.__name}\n"
            f"Age  : {self.__age}"
        )


# -----------------------------

class Student(Person):

    def __init__(self, name, age, roll_number, gpa):
        super().__init__(name, age)

        self.__roll_number = roll_number
        self.__gpa = gpa

    # Getters
    def get_roll_number(self):
        return self.__roll_number

    def get_gpa(self):
        return self.__gpa

    # Setters
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def set_gpa(self, gpa):
        if 0 <= gpa <= 4:
            self.__gpa = gpa
        else:
            print("Invalid GPA!")

    def __str__(self):
        return (
            super().__str__()
            + f"\nRoll Number : {self.__roll_number}"
            + f"\nGPA         : {self.__gpa}"
        )


# -----------------------------

class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary

    # Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

    def work(self):
        return "Employee is working."

    def __str__(self):
        return (
            super().__str__()
            + f"\nEmployee ID : {self.__employee_id}"
            + f"\nSalary      : Rs.{self.__salary}"
        )


# -----------------------------

class Teacher(Employee):

    def __init__(self, name, age, employee_id, salary, subject, experience):
        super().__init__(name, age, employee_id, salary)

        self.__subject = subject
        self.__experience = experience

    # Getters
    def get_subject(self):
        return self.__subject

    def get_experience(self):
        return self.__experience

    # Setters
    def set_subject(self, subject):
        self.__subject = subject

    def set_experience(self, experience):
        if experience >= 0:
            self.__experience = experience
        else:
            print("Invalid experience!")

    # Method Overriding
    def work(self):
        return f"Teaching {self.__subject}."

    def __str__(self):
        return (
            super().__str__()
            + f"\nSubject     : {self.__subject}"
            + f"\nExperience  : {self.__experience} Years"
        )


# -----------------------------
# Object Creation
# -----------------------------

student1 = Student(
    "Rijan Pariyar",
    21,
    "ST101",
    3.95
)

teacher1 = Teacher(
    "Bishal Prashad Kurmi",
    35,
    "EMP201",
    85000,
    "Python Programming",
    10
)

print("Student Details")
print(student1)

print("\n---------------------------\n")

print("Teacher Details")
print(teacher1)
print(teacher1.work())

# -----------------------------
# Updating Details
# -----------------------------

student1.set_gpa(4.0)

teacher1.set_salary(90000)
teacher1.set_subject("Object-Oriented Programming")
teacher1.set_experience(12)

print("\nAfter Updating Details\n")

print(student1)

print()

print(teacher1)
print(teacher1.work())