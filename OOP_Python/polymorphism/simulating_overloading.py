class Calculator:

    def multiply(self, a, b, c=None, d=None):

        if c is None and d is None:
            return a * b

        elif d is None:
            return a * b * c

        else:
            return a * b * c * d


cal = Calculator()

print(cal.multiply(2, 3))
print(cal.multiply(2, 3, 4))
print(cal.multiply(2, 3, 4, 5))