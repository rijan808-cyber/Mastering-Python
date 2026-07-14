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


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary.")

    def __str__(self):
        return (
            super().__str__()
            + f"\nEmployee ID : {self.__employee_id}"
            + f"\nSalary      : Rs.{self.__salary}"
        )

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def __str__(self):
        return (
            super().__str__()
            + f"\nDepartment  : {self.__department}"
        )

manager1 = Manager(
    "Rijan Pariyar",
    21,
    "EMP101",
    75000,
    "Information Technology"
)

print("Manager Details")
print(manager1)

manager1.set_salary(85000)
manager1.set_department("Cyber Security")

print("\nAfter Updating Details")
print(manager1)