# Fibonacci series generator
def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the series
    series = [0, 1]
    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

# Input number of terms
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_series(num_terms)
print("Fibonacci series:", result)
