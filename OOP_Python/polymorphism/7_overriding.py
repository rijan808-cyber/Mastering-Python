class Father:
    def arrangement(self):
        print('Marriage Arrangement Successfully Done')
    
    def demand(self):
        print('Car/Gold/Cash/Others..')

    def marry(self):
        print('Marry to Kajol..')

class Son(Father):
    def marry(self):
        print('Marry to Katrina...')
    
    

s=Son()
s.arrangement()
s.demand()
s.marry()