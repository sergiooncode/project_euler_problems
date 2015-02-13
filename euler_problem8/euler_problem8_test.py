try:
    import euler_problem8
except ImportError:
    raise SystemExit('Couldnt find euler_problem8.py. Does it exist?')

import unittest

class EulerProblem8Tests(unittest.TestCase):
    def setUp(self):
        self.e = euler_problem8.EulerProblem8()

    def test_countDigitsInTheNumber(self):
        self.assertEqual(
            1000,
            self.e.count()
        )

    def test_getSliceOfFourStartingAtFirstElement(self):
        self.assertEqual(
                "7316",
                self.e.get_slice(0, 4)
                )

    def test_getSliceOfFourStartingAtSecondElement(self):
        self.assertEqual(
                "3167",
                self.e.get_slice(1, 5)
                )

    def test_getLastSliceOfFour(self):
        self.assertEqual(
                "3450",
                self.e.get_slice(996, 1000)
                )

    def test_findFourAdjacentWithGreatestProduct(self):
        self.assertEqual(
                5832,
                self.e.find_greatest_product_of(13)
                )

    def test_findThirteenAdjacentWithGreatestProduct(self):
        self.assertEqual(
                23514624000,
                self.e.find_greatest_product_of(13)
                )

if __name__ == '__main__':
    unittest.main()
