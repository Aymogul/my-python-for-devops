def calculator():
    """Simple calculator program with error handling and extra operations."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid number. Please enter a valid numeric value.")
            continue