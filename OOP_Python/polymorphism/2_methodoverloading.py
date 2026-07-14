class ABC:
    def walk(self):
        print('Walk with 0 argument')
    def walk(self,a):
        print(f'Walk with 1 argument {a}')
    def walk(self,a,b):
        print(f'Walk with 2 argument {a} and {b}')
    def walk(self,a,b,c):
        print(f'Walk with 3 argument {a}, {b} and {c}')

obj=ABC()
obj.walk(2,4,6)
