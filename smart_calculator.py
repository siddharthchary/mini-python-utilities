# smart_calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("\n--- SMART CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Choose operation (1-4): "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

while True:
    calculator()
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break
