# Level 3: CLI-based Calculator (loop until quit)

# Define basic arithmetic functions
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    # Prevent division by zero
    return a / b if b != 0 else "Error: Division by zero"

def calculator():
    # Welcome message
    print("Simple CLI Calculator")
    print("Type 'quit' to exit.")

    # Loop until user types 'quit'
    while True:
        # Ask user to choose an operation
        op = input("Choose operation (+, -, *, /): ").strip()

        # Exit condition
        if op.lower() == "quit":
            print("Goodbye!")
            break

        # Get user input for numbers
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            # Handle invalid input (e.g., letters instead of numbers)
            print("Invalid input. Please enter numbers only.")
            continue

        # Perform calculation based on chosen operation
        if op == '+':
            print("Result:", add(a, b))
        elif op == '-':
            print("Result:", subtract(a, b))
        elif op == '*':
            print("Result:", multiply(a, b))
        elif op == '/':
            print("Result:", divide(a, b))
        else:
            # Handle invalid operation symbols
            print("Invalid operation")

# Run the calculator
calculator()
