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

# Unit tests for the above functions
if __name__ == "__main__":
    import unittest

    class TestFunctions(unittest.TestCase):
        def test_is_prime(self):
            self.assertTrue(is_prime(2))
            self.assertTrue(is_prime(3))
            self.assertFalse(is_prime(4))
            self.assertFalse(is_prime(1))
            self.assertTrue(is_prime(17))

        def test_calculate_fibonacci(self):
            self.assertEqual(calculate_fibonacci(0), [])
            self.assertEqual(calculate_fibonacci(1), [0])
            self.assertEqual(calculate_fibonacci(2), [0, 1])
            self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])

        def test_sum_of_primes_in_fibonacci(self):
            self.assertEqual(sum_of_primes_in_fibonacci(0), 0)
            self.assertEqual(sum_of_primes_in_fibonacci(1), 0)
            self.assertEqual(sum_of_primes_in_fibonacci(2), 0)
            self.assertEqual(sum_of_primes_in_fibonacci(5), 5)  # Only 2 and 3 are primes in [0, 1, 1, 2, 3]

    unittest.main()
