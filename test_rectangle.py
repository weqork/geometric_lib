import unittest
from rectangle import ( 
    area as rectangle_area, perimeter as rectangle_perimeter
)


class RectangleTestCase(unittest.TestCase):
        
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
