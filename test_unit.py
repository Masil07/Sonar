import unittest

class TestFibonacciPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        # Testing prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

        # Testing non-prime numbers
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))

    def test_is_prime_duplicate(self):
        # Testing prime numbers for duplicate function
        self.assertTrue(is_prime_duplicate(2))
        self.assertTrue(is_prime_duplicate(3))
        self.assertTrue(is_prime_duplicate(5))
        self.assertTrue(is_prime_duplicate(7))
        self.assertTrue(is_prime_duplicate(11))

        # Testing non-prime numbers for duplicate function
        self.assertFalse(is_prime_duplicate(1))
        self.assertFalse(is_prime_duplicate(4))
        self.assertFalse(is_prime_duplicate(8))
        self.assertFalse(is_prime_duplicate(10))
        self.assertFalse(is_prime_duplicate(15))

    def test_calculate_fibonacci(self):
        # Testing Fibonacci sequence generation
        self.assertEqual(calculate_fibonacci(0), [])
        self.assertEqual(calculate_fibonacci(1), [0])
        self.assertEqual(calculate_fibonacci(2), [0, 1])
        self.assertEqual(calculate_fibonacci(3), [0, 1, 1])
        self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(calculate_fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_calculate_fibonacci_duplicate(self):
        # Testing Fibonacci sequence generation for duplicate function
        self.assertEqual(calculate_fibonacci_duplicate(0), [])
        self.assertEqual(calculate_fibonacci_duplicate(1), [0])
        self.assertEqual(calculate_fibonacci_duplicate(2), [0, 1])
        self.assertEqual(calculate_fibonacci_duplicate(3), [0, 1, 1])
        self.assertEqual(calculate_fibonacci_duplicate(5), [0, 1, 1, 2, 3])
        self.assertEqual(calculate_fibonacci_duplicate(7), [0, 1, 1, 2, 3, 5, 8])

    def test_sum_of_primes_in_fibonacci(self):
        # Testing the sum of primes in Fibonacci sequence
        self.assertEqual(sum_of_primes_in_fibonacci(0), 0)
        self.assertEqual(sum_of_primes_in_fibonacci(1), 0)
        self.assertEqual(sum_of_primes_in_fibonacci(2), 2)
        self.assertEqual(sum_of_primes_in_fibonacci(5), 5)  # Primes: 2, 3
        self.assertEqual(sum_of_primes_in_fibonacci(7), 10)  # Primes: 2, 3, 5

    def test_sum_of_primes_in_fibonacci_duplicate(self):
        # Testing the sum of primes in Fibonacci sequence for duplicate function
        self.assertEqual(sum_of_primes_in_fibonacci_duplicate(0), 0)
        self.assertEqual(sum_of_primes_in_fibonacci_duplicate(1), 0)
        self.assertEqual(sum_of_primes_in_fibonacci_duplicate(2), 2)
        self.assertEqual(sum_of_primes_in_fibonacci_duplicate(5), 5)  # Primes: 2, 3
        self.assertEqual(sum_of_primes_in_fibonacci_duplicate(7), 10)  # Primes: 2, 3, 5

    def test_is_prime_another_duplicate(self):
        # Testing prime numbers for another duplicate function
        self.assertTrue(is_prime_another_duplicate(2))
        self.assertTrue(is_prime_another_duplicate(3))
        self.assertTrue(is_prime_another_duplicate(5))
        self.assertTrue(is_prime_another_duplicate(7))
        self.assertTrue(is_prime_another_duplicate(11))

        # Testing non-prime numbers for another duplicate function
        self.assertFalse(is_prime_another_duplicate(1))
        self.assertFalse(is_prime_another_duplicate(4))
        self.assertFalse(is_prime_another_duplicate(8))
        self.assertFalse(is_prime_another_duplicate(10))
        self.assertFalse(is_prime_another_duplicate(15))

    def test_calculate_fibonacci_another_duplicate(self):
        # Testing Fibonacci sequence generation for another duplicate function
        self.assertEqual(calculate_fibonacci_another_duplicate(0), [])
        self.assertEqual(calculate_fibonacci_another_duplicate(1), [0])
        self.assertEqual(calculate_fibonacci_another_duplicate(2), [0, 1])
        self.assertEqual(calculate_fibonacci_another_duplicate(3), [0, 1, 1])
        self.assertEqual(calculate_fibonacci_another_duplicate(5), [0, 1, 1, 2, 3])
        self.assertEqual(calculate_fibonacci_another_duplicate(7), [0, 1, 1, 2, 3, 5, 8])

    def test_sum_of_primes_in_fibonacci_another_duplicate(self):
        # Testing the sum of primes in Fibonacci sequence for another duplicate function
        self.assertEqual(sum_of_primes_in_fibonacci_another_duplicate(0), 0)
        self.assertEqual(sum_of_primes_in_fibonacci_another_duplicate(1), 0)
        self.assertEqual(sum_of_primes_in_fibonacci_another_duplicate(2), 2)
        self.assertEqual(sum_of_primes_in_fibonacci_another_duplicate(5), 5)  # Primes: 2, 3
        self.assertEqual(sum_of_primes_in_fibonacci_another_duplicate(7), 10)  # Primes: 2, 3, 5

if __name__ == "__main__":
    unittest.main()
