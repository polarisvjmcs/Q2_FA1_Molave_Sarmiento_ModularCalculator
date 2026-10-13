# Version 2: Improved Modular Calculator
# Added input validation and clearer output formatting.

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        result = add_numbers(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract_numbers(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply_numbers(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")

    elif choice == "4":
        result = divide_numbers(num1, num2)

        if result is None:
            print("\nCannot divide by zero.")
        else:
            print(f"\nResult: {num1} / {num2} = {result}")

    else:
        print("\nInvalid operation choice.")

except ValueError:
    print("\nInvalid input. Please enter numbers only.")
