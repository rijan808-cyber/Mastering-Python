class Human:
    def __init__(self):
        print('Parent Constructor..')
    def walk(self):
        print("Walking...")
    def sleep(self):
        print('Sleeping')
 
class Student(Human):
    
    def read(self):
        print("reading")

s=Student()
s.read()
s.walk()