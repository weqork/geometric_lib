import unittest
from square import ( 
    area as square_area, perimeter as square_perimeter
)


class SquareTestCase(unittest.TestCase):
        
    def test_square_area(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(0), 0)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(0), 0)
