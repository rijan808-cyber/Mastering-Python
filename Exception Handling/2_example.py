
print("Hello World")
try:
    print(10/5)
    a=5+"Bishal"
except ZeroDivisionError as msg:
    print(10/2)
except ValueError as msg:
    print('Value error Hnadled..')
except: 
    print('unkown Error handled..')
print('Lbef')