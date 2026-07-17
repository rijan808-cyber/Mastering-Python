from abc import *
class Person(ABC):
    def speak(self):
        print("Speak..")

    @abstractmethod
    def success(self):
        pass

class Student(Person):
    def success(self):
        print("Success by doing smart and hard work..")

    def move(self):
        print("Moving..")

s1 = Student()
s1.speak()
s1.success()