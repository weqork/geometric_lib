import unittest

from triangle import (
    area as triangle_area, perimeter as triangle_perimeter
)

class TriangleTestCase(unittest.TestCase):
    
    def test_triangle_area_good(self):
        self.assertEqual(triangle_area(6, 4), 12)
    
    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(0, 4), 0)
    
    def test_triangle_area_bad(self):
        self.assertEqual(triangle_area(-6, 4), "ValueError")

    def test_triangle_area_bad(self):
        self.assertEqual(triangle_area(6, -4), "ValueError")
    
    def test_triangle_perimeter_good(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
    
    def test_triangle_perimeter_bad(self):
        self.assertEqual(triangle_perimeter(-3, 4, 5), "ValueError")

    def test_triangle_perimeter_bad(self):
        self.assertEqual(triangle_perimeter(3, -4, 5), "ValueError")

    def test_triangle_perimeter_bad(self):
        self.assertEqual(triangle_perimeter(3, 4, -5), "ValueError")
