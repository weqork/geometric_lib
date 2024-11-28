import unittest
from triangle import ( 
    area as triangle_area, perimeter as triangle_perimeter
)


class TriangleTestCase(unittest.TestCase):
        
    def test_triangle_area(self):
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_area(0, 4), 0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
