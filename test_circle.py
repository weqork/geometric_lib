import unittest
import math

from circle import ( 
    area as circle_area, perimeter as circle_perimeter
)


class GeometryTestCase(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25, places=1)
        self.assertEqual(circle_area(0), 0)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5, places=1)
        self.assertEqual(circle_perimeter(0), 0)

