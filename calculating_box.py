def calculator():
    """Simple calculator program with error handling and extra operations."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid number. Please enter a valid numeric value.")
            continue

        operation = input("Choose operation (+, -, *, /, **, %): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("❌ Error: Cannot divide by zero.")
                continue
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '%':
            result = num1 % num2
        else:
            print("⚠️ Invalid operation. Please try again.")
            continue

        print(f"✅ Result: {result}")

        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() != 'yes':
            print("👋 Goodbye!")
            break


# Run the calculator
calculator()
