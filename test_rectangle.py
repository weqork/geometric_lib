import unittest

from rectangle import (
    area as rectangle_area, perimeter as rectangle_perimeter
)

class RectangleTestCase(unittest.TestCase):
    
    def test_rectangle_area_good(self):
        self.assertEqual(rectangle_area(5, 10), 50)
    
    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle_area(5, 0), 0)
    
    def test_rectangle_area_bad1(self):
        self.assertEqual(rectangle_area(-5, 10), "ValueError")

    def test_rectangle_area_bad2(self):
        self.assertEqual(rectangle_area(5, -10), "ValueError")
        
    def test_rectangle_area_string1(self):
        self.assertEqual(rectangle_area("a", 10), "ValueError")
        
    def test_rectangle_area_string2(self):
        self.assertEqual(rectangle_area(5, "a"), "ValueError")
    
    def test_rectangle_perimeter_good(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
    
    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
    
    def test_rectangle_perimeter_bad1(self):
        self.assertEqual(rectangle_perimeter(-5, 10), "ValueError")

    def test_rectangle_perimeter_bad2(self):
        self.assertEqual(rectangle_perimeter(5, -10), "ValueError")
        
    def test_rectangle_perimeter_string1(self):
        self.assertEqual(rectangle_area("a", 10), "ValueError")
        
    def test_rectangle_perimeter_string2(self):
        self.assertEqual(rectangle_area(5, "a"), "ValueError")
