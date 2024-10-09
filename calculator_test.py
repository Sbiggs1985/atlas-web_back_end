import unittest
from calculator import calculator

class TestCalculator(unittest.TextCase):


    def setUp(self):
        self.calc = Calculator()
    
    
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
            
if __name__ == '__main__':
    unittest.main()