import random
import unittest
from lab_2 import monte_carlo_area

class TestMonteCarloArea(unittest.TestCase):

    def test_area_n_100(self):
        random.seed(1)
        result = monte_carlo_area(100)
        self.assertAlmostEqual(result, 2.64, places=7)

    def test_area_n_1000(self):
        random.seed(1)
        result = monte_carlo_area(1000)
        self.assertAlmostEqual(result, 2.316, places=7)

    def test_area_n_10000(self):
        random.seed(1)
        result = monte_carlo_area(10000)
        self.assertAlmostEqual(result, 2.0052, places=7)

if __name__ == '__main__':
    unittest.main()