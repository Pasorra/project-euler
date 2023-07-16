import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_factorize(self):
        self.assertEqual(utils.factorize(1), [])
        self.assertEqual(utils.factorize(-4), [])
        self.assertEqual(utils.factorize(2), [2])
        self.assertEqual(utils.factorize(12), [2, 2, 3])
        self.assertEqual(utils.factorize(20), [2, 2, 5])

    def test_completely_factorize(self):
        self.assertEqual(utils.completely_factorize(5), [1, 5])
        self.assertEqual(utils.completely_factorize(-4), [])
        self.assertEqual(utils.completely_factorize(20), [1, 2, 4, 5, 10, 20])

    def test_is_palindrome(self):
        self.assertTrue(utils.is_palindrome("a"))
        self.assertFalse(utils.is_palindrome("ab"))
        self.assertTrue(utils.is_palindrome(""))
        self.assertTrue(utils.is_palindrome("12321"))

    def test_is_prime(self):
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(5))
        self.assertFalse(utils.is_prime(10))
        self.assertFalse(utils.is_prime(1))
        self.assertFalse(utils.is_prime(-20))
        self.assertFalse(utils.is_prime(0))

    def test_sieve(self):
        self.assertEqual(utils.sieve(10), {2, 3, 5, 7})
        self.assertEqual(utils.sieve(11), {2, 3, 5, 7})
        self.assertEqual(utils.sieve(2), set())
        with self.assertRaises(IndexError):
            utils.sieve(1)
        with self.assertRaises(ValueError):
            utils.sieve(-1)


if __name__ == "__main__":
    unittest.main()
