class ABC:
    def walk(self,a=0,b=0,c=0):
        print(f'Walk with argument {a}, {b} and {c}')

obj=ABC()
obj.walk(2,4,6)
obj.walk()
obj.walk(100)
