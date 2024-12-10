# This program attempts to calculate the factorial of a number, but it has many bugs.

def factorial(n):
    # Missing parameter type check, potential for non-integer input
    if n < 0:
        print("Error: Negative numbers are not allowed!")
        return 0

    result = 1
    # Incorrect loop, will cause an infinite loop if n > 1
    for i in range(1, n):  # Off-by-one error, should be 'n + 1'
        result *= i

    # Potential for division by zero if n is zero
    return result / n  # Incorrect return type (should be an integer, not float)

# User input without validation
num = input("Enter a number to calculate its factorial: ")  # User input not converted to integer

# Missing try-except block for error handling
print("The factorial of", num, "is", factorial(num))  # Will raise a TypeError if input is not an int
