def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_fibonacci(n):
    """Generate a Fibonacci sequence up to n terms."""
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

def sum_of_primes_in_fibonacci(n):
    """Calculate the sum of prime numbers in the Fibonacci sequence up to n terms."""
    if n < 1:
        return 0
    fibonacci_series = calculate_fibonacci(n)
    prime_sum = sum(num for num in fibonacci_series if is_prime(num))
    return prime_sum
