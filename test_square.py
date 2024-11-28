import unittest
from square import ( 
    area as square_area, perimeter as square_perimeter
)


class SquareTestCase(unittest.TestCase):
        
    def test_square_area_good(self):
        self.assertEqual(square_area(5), 25)

    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_square_area_bad(self):
        self.assertEqual(square_area(-5), "ValueError")

    def test_square_perimeter_good(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_bad(self):
        self.assertEqual(square_perimeter(-5), "ValueError")
        
    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
    
        
