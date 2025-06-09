# This is the main file of our program. It is responsible for starting the calculator application.
# we import the calculator function from the calculator module.
from app.calculator import calculator


#__name__ is a special variable in Python that is set to "__main__" when the script is run directly.
if __name__ == "__main__":
    # Now, we use the calculator function to start the calculator application.
    # This function will run an infinite loop, allowing the user to perform calculations until they choose to exit.
    calculator()
