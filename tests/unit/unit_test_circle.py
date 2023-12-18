import unittest
import circle
from circle import area, perimeter

class CircleTest(unittest.TestCase):
    def test_area_int(self):
        self.assertAlmostEqual(area(8), 201.06192982974676)

    def test_area_float(self):
        self.assertAlmostEqual(area(9.31), 272.30099900181426)
    def test_area_0(self):
        self.assertAlmostEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-15)



    def test_perimeter_int(self):
        self.assertAlmostEqual(perimeter(8), 50.26548245743669)

    def test_perimter_float(self):
        self.assertAlmostEqual(perimeter(9.31), 58.49645520984195)

    def test_perimeter_0(self):
        self.assertAlmostEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-15)


if __name__ == '__main__':
    unittest.main()