import unittest
import math

from circle import (
    area as circle_area, perimeter as circle_perimeter
)

class CircleTestCase(unittest.TestCase):
    
    def test_circle_area_good(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25, places=1)
    
    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)
    
    def test_circle_area_bad(self):
        self.assertEqual(circle_area(-5), "ValueError")

    def test_circle_area_string(self):
        self.assertEqual(circle_area("a"), "ValueError")
    
    def test_circle_perimeter_good(self):
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5, places=1)
    
    def test_circle_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)
    
    def test_circle_perimeter_bad(self):
        self.assertEqual(circle_perimeter(-5), "ValueError")
        
    def test_circle_perimeter_string(self):
        self.assertEqual(circle_perimeter("a"), "ValueError")
