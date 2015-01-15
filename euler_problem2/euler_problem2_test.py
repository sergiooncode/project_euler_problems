try:
    import euler_problem2
except ImportError:
    raise SystemExit('Could not find euler_problem2.py. Does it exist?')

import unittest

class EulerProblem2Tests(unittest.TestCase):
    def setUp(self):
        self.e = euler_problem2.EulerProblem2()

    def test_generateTermsLessThanThree(self):
        self.assertEqual(
            [1, 2],
            self.e.generate(3)
        )

    def test_generateTermsLessThanFour(self):
        self.assertEqual(
            [1, 2, 3],
            self.e.generate(4)
        )

    def test_generateTermsLessThanFive(self):
        self.assertEqual(
            [1, 2, 3, 5],
            self.e.generate(6)
        )

    def test_generateTermsLessThan9(self):
        self.assertEqual(
            [1, 2, 3, 5, 8],
            self.e.generate(9)
        )

    def test_sumEvenTermsLessThanThree(self):
        self.assertEqual(
            2,
            self.e.sum_even_terms(3)
        )

    def test_sumEvenTermsLessThanFour(self):
        self.assertEqual(
            2,
            self.e.sum_even_terms(4)
        )

    def test_sumEvenTermsLessThanSix(self):
        self.assertEqual(
            2,
            self.e.sum_even_terms(6)
        )

    def test_sumEvenTermsLessThanNine(self):
        self.assertEqual(
            10,
            self.e.sum_even_terms(9)
        )

    def test_generateTermsLessThanFourMillion(self):
        self.assertEqual(
            4613732,
            self.e.sum_even_terms(4000000)
        )

if __name__ == '__main__':
    unittest.main()
