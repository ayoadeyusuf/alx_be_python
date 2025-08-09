import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.asserEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(4, 245), 249)
        self.assertEqual(self.calc.add(-7, -1), -8)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -2), -7)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(7, -1), 8)
        self.assertEqual(self.calc.subtract(7, 1), 6)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(0, -3), 0)
    def test_division(self):
      self.assertEqual(self.calc.divide(4, 2), 2)
      self.assertEqual(self.calc.divide(4, -2), -2)
      self.assertEqual(self.calc.divide(-4, 2), -2)
      self.assertEqual(self.calc.divide(-4, -2), 2)
      self.assertEqual(self.calc.divide(2, 4), 0.5)
      self.assertEqual(self.calc.divide(4, 0), None)
      self.assertEqual(self.calc.divide(0, -2), 0)
      
      
      
