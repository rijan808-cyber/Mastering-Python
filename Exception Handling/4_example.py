
print("Hello World")
try:
    a=5+"Bishal"
except ZeroDivisionError as msg:
    print(10/2)
except ValueError as msg:
    print('Value error Hnadled..')
except TypeError as msg:
    print('Type error Hnadled..')
finally:
    print('Clean up the code..')
print('Lbef')