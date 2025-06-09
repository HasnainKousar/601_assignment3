"""
tests/test_operations.py

This module contains test cases for the Operation class, which includes methods 
for basic arithmetic operations: addition, subtraction, multiplication, and division.

We use parametrization with pytest to test various scenarios for each operation.
This will allow us to efficiently test multiple scenarios with different inputs,
and ensure that the methods behave as expected.

Parametrization tests help in validating the correctness of the methods
by checking against expected results for a variety of inputs, including edge cases.

The tests also include checks for division by zero, which should raise a ValueError.
"""

import pytest # Importing pytest for testing framework
from typing import Union # Importing Union for type hinting
from app.operations import Operation # Importing the Operation class from the operations module



Number = Union[int, float]  # Type alias for numbers that can be either int or float


# Test cases for the Operation class methods

#----------------------------------------------------------------
# Test cases for the 'add' method
#----------------------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 4, 5),  # Positive integers
        (-1, -2, -3),  # Negative integers
        (1.5, 2.5, 4.0),  # Positive floats
        (-1.5, 3.5, 2), # Negative floats
        (-2, 4, 2),  # negative and positive integers
        (0.0, 0.0, 0.0), # testing with zero
    ],
    ids=[
        "positive_integers",
        "negative_integers",
        "positive_floats",
        "negative_floats",
        "mixed_integers",
        "zero_case"
    ]
   
)
def test_add(a: Number, b: Number, expected: Number):
    """
    Test the add method of the Operation class.

    This function uses pytest's parametrize feature to test various cases of addition.
    It includes tests for addition of positive integers, negative integers,
    positive floats, cases involving zero, etc.
    Each test case consists of two input values (a and b) and the expected result.
    By using paramerization, we can easily test multiple scenarios without writing separate test functions for each case.

    Parameters:
    a (number): First number to add.
    b (number): Second number to add.
    expected (Number): Expected result of the addition.

    steps:
    1. Call the add method with the provided inputs a and b.
    2. Compare the result with the expected value.
    3. Assert that the result matches the expected value.

    Example:
    >>> test_add(1, 4, 5)
    >>> test_add(-1, -2, -3)
    """

    # Call the add method with the provided inputs a and b
    result = Operation.add(a, b)

    # Compare the result with the expected value
    assert result == expected, f"Expected {expected}, but got {result} for add({a}, {b})"


#----------------------------------------------------------------
# Test cases for the 'subtract' method
#----------------------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),  # Positive integers
        (-1, -2, 1),  # Negative integers
        (2.5, 1.5, 1.0),  # Positive floats
        (-3.5, -1.5, -2.0), # Negative floats
        (4, -2, 6),  # positive and negative integers
        (0.0, 0.0, 0.0), # testing with zero
    ],
    ids=[
        "positive_integers",
        "negative_integers",
        "positive_floats",
        "negative_floats",
        "mixed_integers",
        "zero_case"
    ]
)
def test_subtract(a: Number, b: Number, expected: Number):
    """
    Test the subtract method of the Operation class.

    This function uses pytest's parametrize feature to test various cases of subtraction.
    It includes tests for subtraction of positive integers, negative integers,
    positive floats, cases involving zero, etc.
    Each test case consists of two input values (a and b) and the expected result.
    By using paramerization, we can easily test multiple scenarios without writing separate test functions for each case.

    Parameters:
    a (Number): First Number to subtract from.
    b (Number): Second Number to subtract.
    expected (Number): Expected result of the subtraction.


    steps:
    1. Call the subtract method with the provided inputs a and b.
    2. Compare the result with the expected value.
    3. Assert that the result matches the expected value.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-1, -2, 1)
    """

    # Call the subtract method with the provided inputs a and b
    result = Operation.subtract(a, b)

    # Compare the result with the expected value
    assert result == expected, f"Expected {expected}, but got {result} for subtract({a}, {b})"


#----------------------------------------------------------------
# Test cases for the 'multiply' method
#----------------------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),  # Positive integers
        (-1, -2, 2),  # Negative integers
        (1.5, 2.0, 3.0),  # Positive floats
        (-1.5, -2.0, 3.0), # Negative floats
        (4, -2, -8),  # positive and negative integers
        (0.0, 5.0, 0.0), # testing with zero
    ],
    ids=[
        "positive_integers",
        "negative_integers",
        "positive_floats",
        "negative_floats",
        "mixed_integers",
        "zero_case"
    ]
)
def test_multiply(a: Number, b: Number, expected: Number):
    """
    Test the multiply method of the Operation class.

    This function uses pytest's parametrize feature to test various cases of multiplication.
    It includes tests for multiplication of positive integers, negative integers,
    positive floats, cases involving zero, etc.
    Each test case consists of two input values (a and b) and the expected result.
    By using paramerization, we can easily test multiple scenarios without writing separate test functions for each case.

    Parameters:
    a (number): First number to multiply.
    b (number): Second number to multiply.

    steps:
    1. Call the multiply method with the provided inputs a and b.
    2. Compare the result with the expected value.
    3. Assert that the result matches the expected value.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-1, -2, 2)
    """

    # Call the multiply method with the provided inputs a and b
    result = Operation.multiply(a, b)

    # Compare the result with the expected value
    assert result == expected, f"Expected {expected}, but got {result} for multiply({a}, {b})"


#----------------------------------------------------------------
# Test cases for the 'divide' method
#----------------------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),  # Positive integers
        (-4, -2, 2),  # Negative integers
        (5.0, 2.5, 2.0),  # Positive floats
        (-7.5, -2.5, 3.0), # Negative floats
        (8, -4, -2),  # positive and negative integers
        (0.0, 1.0, 0.0), # testing with zero
    ],
    ids=[
        "positive_integers",
        "negative_integers",
        "positive_floats",
        "negative_floats",
        "mixed_integers",
        "zero_case"
    ]
)


def test_divide(a: Number, b: Number, expected: float):
    """
    Test the divide method of the Operation class.

    This function uses pytest's parametrize feature to test various cases of division.
    It includes tests for division of positive integers, negative integers,
    positive floats, cases involving zero, etc.
    Each test case consists of two input values (a and b) and the expected result.
    By using paramerization, we can easily test multiple scenarios without writing separate test functions for each case.

    Parameters:
    a (Number): Numerator.
    b (Number): Denominator.
    expected (float): Expected result of the division.

    steps:
    1. Call the divide method with the provided inputs a and b.
    2. Compare the result with the expected value.
    3. Assert that the result matches the expected value.

    Example:
    >>> test_divide(6, 3, 2)
    >>> test_divide(-4, -2, 2)
    """

    # Call the divide method with the provided inputs a and b
    result = Operation.divide(a, b)

    # Compare the result with the expected value
    assert result == expected, f"Expected {expected}, but got {result} for divide({a}, {b})"



#----------------------------------------------------------------
# Test cases for division by zero
#----------------------------------------------------------------


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),  # Division by zero with integers
        (5.0, 0.0),  # Division by zero with floats
        (-3, 0),  # Negative integer division by zero
        (0, 0),  # Zero division by zero
    ],
    ids=[
        "int_divide_by_zero",
        "float_divide_by_zero",
        "negative_int_divide_by_zero",
        "zero_divide_by_zero"
    ]
)
def test_divide_by_zero(a: Number, b: Number):
    """
    Test the divide method of the Operation class for division by zero.

    This function uses pytest's parametrize feature to test various cases of division by zero.
    Each test case consists of two input values (a and b) where b is zero.
    The expected behavior is that a ValueError should be raised.

    Parameters:
    a (number): Numerator.
    b (number): Denominator, which is expected to be zero.

    steps:
    1. Call the divide method with the provided inputs a and b.
    2. Use pytest's raises context manager to assert that a ValueError is raised.
    3. Assert that a ValueError is raised with the message "Cannot divide by zero."

    Example:
    >>> test_divide_by_zero(1, 0)
    >>> test_divide_by_zero(5.0, 0.0)
    """

    # Assert that a ValueError is raised when dividing by zero
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Operation.divide(a, b)


# The above test cases cover the basic arithmetic operations provided by the Operation class.
# They ensure that the methods work correctly for various types of inputs, including integers, floats, and edge cases like division by zero.
# The use of pytest's parametrize feature allows for efficient testing of multiple scenarios with minimal code duplication.








