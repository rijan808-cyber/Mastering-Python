try:
    print("Outer try block")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Inner Exception: Cannot divide by zero.")
except ValueError:
    print("Outer Exception: Please enter valid integer values.")

print("Program ended.")