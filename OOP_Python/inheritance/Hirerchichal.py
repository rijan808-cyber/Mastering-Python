class Parent:
    def earn(self):
        print('Parent Earning....')

class Child1(Parent):
    def play(self):
        print('Child Playing....')
    
class Child2(Parent):
    def cry(self):
        print('Grand Child crying...')


c=Child1()
c.earn()
c.play()
# c.cry()
