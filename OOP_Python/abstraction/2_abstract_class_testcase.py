from abc import *
class Person(ABC):
    @abstractmethod
    def speak(self):
        print("Rijan Pariyar")

p1 = Person()