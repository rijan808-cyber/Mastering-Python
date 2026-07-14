class Parent1:
    def earn(self):
        print('Parent Earning....')
    
    def money(self):
        print("Parent 1 money ...")

class Parent2:
    def play(self):
        print('Child Playing....')
    
    def money(self):
        print("Parent 2 money ...")
    
class Child(Parent2,Parent1):
    def cry(self):
        print('Grand Child crying...')


c=Child()
c.money()
c.earn()
c.play()
c.cry()
