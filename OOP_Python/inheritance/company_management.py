class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid Salary!")

    def work(self):
        return "Employee is working."

    def __str__(self):
        return (
            f"Employee ID : {self.__employee_id}\n"
            f"Name        : {self.__name}\n"
            f"Salary      : Rs.{self.__salary}"
        )


class Developer(Employee):
    def __init__(self, employee_id, name, salary, programming_language):
        super().__init__(employee_id, name, salary)
        self.__programming_language = programming_language

    def get_programming_language(self):
        return self.__programming_language

    def set_programming_language(self, programming_language):
        self.__programming_language = programming_language

    def work(self):
        return f"Developing software using {self.__programming_language}."

    def __str__(self):
        return (
            super().__str__()
            + f"\nProgramming Language : {self.__programming_language}"
        )


class Designer(Employee):
    def __init__(self, employee_id, name, salary, design_software):
        super().__init__(employee_id, name, salary)
        self.__design_software = design_software

    def get_design_software(self):
        return self.__design_software

    def set_design_software(self, design_software):
        self.__design_software = design_software

    def work(self):
        return f"Designing graphics using {self.__design_software}."

    def __str__(self):
        return (
            super().__str__()
            + f"\nDesign Software : {self.__design_software}"
        )

developer = Developer(
    "EMP101",
    "Rijan Pariyar",
    90000,
    "Python"
)

designer = Designer(
    "EMP102",
    "Aayush Sharma",
    70000,
    "Adobe Photoshop"
)

print("Developer Details")
print(developer)
print(developer.work())

print("\n-----------------------------\n")

print("Designer Details")
print(designer)
print(designer.work())

developer.set_salary(95000)
designer.set_design_software("Figma")

print("\nAfter Updating Details\n")

print(developer)
print(developer.work())

print()

print(designer)
print(designer.work())