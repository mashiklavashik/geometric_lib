import unittest

import triangle
from triangle import area, perimeter


class TriangleTest(unittest.TestCase):
    def test_area_int(self):
        self.assertAlmostEqual(area(3, 6), 9)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-7, 12)

    def test_area_float(self):
        self.assertAlmostEqual(area(3.5, 6.8), 11.9)

    def area_test_0(self):
        self.assertAlmostEqual(area(12.1, 0), 0)

    def test_perimeter_int(self):
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-12, 4, 8)

    def test_perimeter_0(self):
        with self.assertRaises(Exception):
            perimeter(0, 98, 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(9.766, 16, 9.01),34.775999999999996 )

if __name__ == '__main__':
    unittest.main()
