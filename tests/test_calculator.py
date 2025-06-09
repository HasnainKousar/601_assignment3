"""
Tests for the calculator application.

This module contains tests for the calculator application,
it will tests for correct operations and error handling scenarios. 
It uses pytest fixtures to simulate user input and capture output.
"""
from app.calculator import calculator
import pytest


#helper funtion
# This function simulates user input for the calculator REPL and captures its output.
def run_calculator_with_inputs(monkeypatch, inputs, capsys):

    """
    Simulate user input for the calculator REPL and capture its output.

    Parameters:
    - monkeypatch: Pytest fixture to mock input().
    - inputs (list): A list of strings representing user inputs.
    - capsys: Pytest fixture to capture stdout and stderr.

    Returns captured output from the calculator function
    """

    # Use monkeypatch to replace the built-in input function with an iterator over the provided inputs.
    # This allows the calculator REPL to read inputs as if they were entered by the user.
    iter_inputs = iter(inputs)
    # The lambda function will return the next input from the iterator each time input() is called.
    monkeypatch.setattr('builtins.input', lambda _: next(iter_inputs))
    
    # Call the calculator function, which will now use the mocked input.
    calculator()

    # Capture the output from the calculator function using capsys.
    # capsys is a pytest fixture that captures output during the test.
    captured = capsys.readouterr() # Read the captured output from stdout and stderr.
    return captured.out # Return the captured output as a string.

#Test addition operation in the calculator REPL.
def test_addition(monkeypatch,capsys):
    """Test addition operation in REPL."""
    inputs = ['+', '4', '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "The result of 4.0 + 5.0 is: 9.0" in output


 
#Test subtraction operation in the calculator REPL.
def test_subtraction(monkeypatch, capsys):
    """Test subtraction operation in REPL."""
    inputs = ['-', '10', '3', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "The result of 10.0 - 3.0 is: 7.0" in output

#Test multiplication operation in the calculator REPL.
def test_multiplication(monkeypatch, capsys):
    """Test multiplication operation in REPL."""
    inputs = ['*', '6', '7', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "The result of 6.0 * 7.0 is: 42.0" in output

#Test division operation in the calculator REPL.
def test_division(monkeypatch, capsys):
    """Test division operation in REPL."""
    inputs = ['/', '8', '2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "The result of 8.0 / 2.0 is: 4.0" in output

#Test division by zero in the calculator REPL.
def test_division_by_zero(monkeypatch, capsys):
    """Test division by zero in REPL."""
    inputs = ['/', '4', '0', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Cannot divide by zero." in output

#Test invalid operation in the calculator REPL.
def test_invalid_operation(monkeypatch, capsys):
    """Test invalid operation in REPL."""
    inputs = ['add', '8', '2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Invalid operation. Please try again." in output

#Test invalid number one input in the calculator REPL.
def test_invalid_number_one(monkeypatch, capsys):
    """Test invalid number input in REPL."""
    inputs = ['+', 'a', '2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Invalid input. Please enter numeric values for the numbers." in output

#Test invalid number two input in the calculator REPL.
def test_invalid_number_two(monkeypatch, capsys):
    """Test invalid number input in REPL."""
    inputs = ['+', '2', 'b', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Invalid input. Please enter numeric values for the numbers." in output



