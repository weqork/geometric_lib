import unittest

from triangle import (
    area as triangle_area, perimeter as triangle_perimeter
)

class TriangleTestCase(unittest.TestCase):
    
    def test_triangle_area_good(self):
        self.assertEqual(triangle_area(6, 4), 12)
    
    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(0, 4), 0)
    
    def test_triangle_area_bad1(self):
        self.assertEqual(triangle_area(-6, 4), "ValueError")

    def test_triangle_area_bad2(self):
        self.assertEqual(triangle_area(6, -4), "ValueError")

    def test_triangle_area_string1(self):
        self.assertEqual(triangle_area(6, "a"), "ValueError")

    def test_triangle_area_string2(self):
        self.assertEqual(triangle_area("a", 4), "ValueError")
    
    def test_triangle_perimeter_good(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
    
    def test_triangle_perimeter_bad1(self):
        self.assertEqual(triangle_perimeter(-3, 4, 5), "ValueError")

    def test_triangle_perimeter_bad2(self):
        self.assertEqual(triangle_perimeter(3, -4, 5), "ValueError")

    def test_triangle_perimeter_bad3(self):
        self.assertEqual(triangle_perimeter(3, 4, -5), "ValueError")

    def test_triangle_perimeter_string1(self):
        self.assertEqual(triangle_perimeter("a", 4, 5), "ValueError")

    def test_triangle_perimeter_string2(self):
        self.assertEqual(triangle_perimeter(3, "a", 5), "ValueError")

    def test_triangle_perimeter_string3(self):
        self.assertEqual(triangle_perimeter(3, 4, "a"), "ValueError")

