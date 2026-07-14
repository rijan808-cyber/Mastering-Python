class A:
    def walk(self):
        print('Walk with 0 argument')
class B(A):
        def walk(self,a,b,c):
            print(f'Walkh 3 ar witgument {a}, {b} and {c}')


obj=B()
obj.walk(2,4,6)
