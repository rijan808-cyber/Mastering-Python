class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

emp = Employee(101, "Ram", 50000)

print("Employee ID:", emp.id)
print("Employee Name:", emp.name)
print("Salary:", emp.salary)