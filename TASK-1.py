#Basic Calculator python program using python 

def basic_calculator():
    print("Welcome to the Basic Calculator!")
    
    # Prompt user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # Display operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the user's choice
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Perform the chosen operation
    if choice == "1":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose a number between 1 and 4.")

# Run the calculator
basic_calculator()