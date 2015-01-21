try:
    import euler_problem4
except ImportError:
    raise SystemExit('Couldnt find euler_problem4.py. Does it exist?')

import unittest

class EulerProblem4Tests(unittest.TestCase):
    def setUp(self):
        self.e = euler_problem4.EulerProblem4()

    def test_isNumber45Palindrome(self):
        self.assertEqual(
            False,
            self.e.is_palindrome(45)

        )

    def test_isNumber44Palindrome(self):
        self.assertEqual(
            True,
            self.e.is_palindrome(44)
        )

    def test_largestPalindromeOfTwo1digitNumbers(self):
        self.assertEqual(
            9,
            self.e.product_palindromes(9, 9)
        )

    def test_largestPalindromeOfTwo2digitNumbers(self):
        self.assertEqual(
            9009,
            self.e.product_palindromes(99, 99)
        )

    def test_largestPalindromeOfTwo3digitNumbers(self):
        self.assertEqual(
            9009,
            self.e.product_palindromes(999, 999)
        )

if __name__ == '__main__':
    unittest.main()
