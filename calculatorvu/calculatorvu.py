def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_float(prompt):
    """Utility function to safely convert user input to a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Function to drive the calculator
def simple_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operations = {'1': add, '2': subtract, '3': multiply, '4': divide}

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in operations:
            num1 = get_float("Enter first number: ")
            num2 = get_float("Enter second number: ")

            result = operations[choice](num1, num2)

            if choice == '4' and num2 == 0:
                print("Error! Division by zero.")
            else:
                print("Result:", result)

            # Ask if the user wants to calculate again
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please select a number between 1 and 4.")

# Run the calculator
simple_calculator()
