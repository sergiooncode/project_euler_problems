try:
    import euler_problem3
except ImportError:
    raise SystemExit('Could find euler_problem3.py. Does it exist?')

import unittest

class EulerProblem3Tests(unittest.TestCase):
    def setUp(self):
        self.e = euler_problem3.EulerProblem3()

    def test_largestPrimeFactorOf6(self):
        self.assertEqual(
            3,
            self.e.largest_factor(6)
        )

    def test_largestPrimeFactorOf210(self):
        self.assertEqual(
            7,
            self.e.largest_factor(210)
        )

    def test_largestPrimeFactorOf24(self):
        self.assertEqual(
            3,
            self.e.largest_factor(24)
        )

    def test_largestPrimeFactorOf13195(self):
        self.assertEqual(
            29,
            self.e.largest_factor(13195)
        )

    def test_largestPrimeFactorOf600851475143(self):
        self.assertEqual(
            6857,
            self.e.largest_factor(600851475143)
        )

if __name__ == '__main__':
    unittest.main()
