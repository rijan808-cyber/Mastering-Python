class Parent:
    def __init__(self, pname, age, salary):
        self.pname=pname
        self.age=age
        self.salary=salary
     
    def __str__(self):
        return f'''Parent name: {self.pname}\nParent Age: 
        {self.age}\nParent Salary: {self.salary}'''

class Child(Parent):
    def __init__(self, cname, id, fees,pname,age,salary):
        super().__init__(pname,age,salary)
        self.cname=cname
        self.id=id
        self.fees=fees
    
    def __str__(self):
        print(super().__str__())
        print()
        return f'Child name: {self.cname}\nChild ID: {self.id}\nChild Fees: {self.fees}'
    

c=Child("Pcps college",12,900000,"Lbef College",27,20000000)
print(c)
