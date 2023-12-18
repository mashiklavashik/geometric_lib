import unittest
from rectangle import area, perimeter


class RectangleTest(unittest.TestCase):
    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(5, -7)

    def test_area_float(self):
        self.assertAlmostEqual(area(8, 13.5), 108)

    def test_area_int(self):
        self.assertAlmostEqual(area(1, 3), 3)

    def test_area_0(self):
        self.assertAlmostEqual(area(0, 89), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(5, -7)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(8, 13.5), 43)

    def test_perimeter_int(self):
        self.assertAlmostEqual(perimeter(1, 3), 8)

    def test_perimeter_0(self):
        with self.assertRaises(Exception):
            perimeter(0, 89)


if __name__ == '__main__':
    unittest.main()
