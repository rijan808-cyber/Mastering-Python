class Parent:
    def earn(self):
        print('Parent Earning....')

class Child(Parent):
    def play(self):
        print('Child Playing....')
    
class GrandChild(Child):
    def cry(self):
        print('Grand Child crying...')


c=GrandChild()
c.earn()
c.play()
c.cry()
