import unittest

import square
from square import area, perimeter


class SquareTest(unittest.TestCase):
    def test_area_int(self):
        self.assertAlmostEqual(area(3), 9)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-99)

    def test_area_float(self):
        self.assertAlmostEqual(area(16.77), 281.2329)

    def test_area_0(self):
        self.assertAlmostEqual(area(0), 0)

    def test_perimeter_int(self):
        self.assertAlmostEqual(perimeter(3), 12)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-99)


    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(16.77), 67.08)

    def test_perimeter_0(self):
        self.assertAlmostEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()