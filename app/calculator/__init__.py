"""
File for the 'app/calculator.py'.
A simple calculator module that provides basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division

This module is designed to be used as a REPL (Read-Eval-Print Loop) for basic arithmetic operations.
It allows users to perform calculations interactively by entering numbers and selecting operations.
It uses the Operation class from the operations module to perform the calculations.

"""

# First we import the Operation class from the operations module.
# The calculator module will use methods such as add, subtract, multiply, and divide from the Operation class to perform calculations.
from app.operations import Operation

# we create a main function called calculator that will serve as the entry point for the calculator REPL.
# This function will handle user input, perform calculations, and display results.

def calculator():
    """Basic calculator function that performs arithmetic operations."""

    # Welcome message for the user.
    print("Welcome to the Calculator REPL! Type 'exit' to quit.")

    # Start an infinite loop to keep the calculator running until the user decides to exit.
    while True:

        # Display the available operations to the user.
        print("Type '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division, or 'exit' to quit.")

        # Prompt the user to enter an operation.
        operation = input("Enter operation: ").strip() # .strip() is used to remove any leading or trailing whitespace from the input.

        # If the user inputs 'exit', break the loop and exit the calculator.
        # Check if the user wants to exit the calculator.
        if operation.lower() == 'exit':
            print("Exiting the app...") # Display a message indicating that the app is exiting.
            break


        # Validate the operation input.
        # If the operation is not one of the expected symbols, prompt the user to try again.
        # This ensures that the user can only perform valid operations.
        # Valid operations are: addition (+), subtraction (-), multiplication (*), and division (/).
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue

        try:
            # Get user input for the first number.
            a = float(input("Enter first number (use digits, e.g., 5 or 2.15): "))

            # Get user input for the second number.
            b = float(input("Enter second number (use digits, e.g., 5 or 2.15): "))

            # Perform the operation based on user input.
            if operation == '+':
                result = Operation.add(a, b) # Call the add method from the Operation class to perform addition.
            
            elif operation == '-':
                result = Operation.subtract(a, b) # Call the subtract method from the Operation class to perform subtraction.
            
            elif operation == '*':
                result = Operation.multiply(a, b) # Call the multiply method from the Operation class to perform multiplication.
            
            else: # else part of the if statement, which means the operation is division.
                # For division, we need to handle the case where the second number is zero.
                # If b is zero, we raise a ValueError to prevent division by zero.
                try:
                    result = Operation.divide(a, b) # Call the divide method from the Operation class to perform division.
                except ValueError as e:
                    print(e)
                    continue
            # Display the result of the operation.
            print(f"The result of {a} {operation} {b} is: {result}")

        except ValueError:
            # Handle the case where the user inputs a non-numeric value.
            print("Invalid input. Please enter numeric values for the numbers.")
        

