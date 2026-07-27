
print("Hello World")
try:
    print(10/5)
    a=5+"Bishal"
except (ZeroDivisionError,ValueError, TypeError) as msg:
    print(f"Occured Exception Hnadled: {msg}")
except: 
    print('unkown Error handled..')
print('Lbef')