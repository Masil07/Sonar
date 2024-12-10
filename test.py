# Fibonacci series generator with bugs
def fibonacci_series(n):
    if n < 0:  # Bug: This condition should be 'n <= 0' to handle non-positive integers properly.
        print("Please enter a positive integer.")
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the series
    series = [0, 1]
    for i in range(1, n):  # Bug: This loop should start from 2, not 1, to ensure correct series generation.
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

# Input number of terms
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_series(num_terms)
print("Fibonacci series:", result)
