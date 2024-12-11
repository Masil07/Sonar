import unittest
from test import is_prime, calculate_fibonacci, sum_of_primes_in_fibonacci

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

if __name__ == "__main__":
    unittest.main()
