# REPL Calculator with Advanced Testing in Python
## Project Overview:

Welcome to the Module 3 assignment, where we create a REPL (Read-Eval-Print Loop) for basic arithmetic operations.
Which allows users to perform calculations interactively by entering numbers and selecting operations.
This project uses Object-Oriented Programming (OOP) principles and advanced testing techniques.

## Object-Oriented Programming and Advanced Testing

For this project, we used Object-Oriented Programming (OOP) principles to create a class called Operation.
This class contained methods for basic arithmetic operations: addition, subtraction, multiplication, and division.
Instead of creating a separate function for each operation, we defined static methods within the Operation class.
Static methods allow us to call these methods without needing to create an instance of the class. This allows us to group related operations together and makes the code more organized and reusable.

We use parametrization with pytest to test various scenarios for each operation. This allowed us to efficiently test multiple scenarios with different inputs, and ensure that the methods behave as expected. Parametrization tests help in validating the correctness of the methods by checking against expected results for a variety of inputs, including edge cases.

## Features
- Interactive REPL Calculator: User can perform basic calculations interactively by entering numbers and selecting operations in a loop.
- Object_Oriented Design: Arithmetic operations are implemented as static methods within the Operation class to promote code reusability and organization.
- Error Handling: Handling invalid inputs and division by zero by providing user-friendly messages. 
- User-Friendly Interface: Clear prompts and instruction to guide user through the calculation process
- Advance Testing: Uses parametrization with pytest to test various scenarios for each operation

## Setup Instruction

