import unittest
from math_operations import add, subtract, multiply, divide, power, modulo

class TestMathOperations(unittest.TestCase):

    # Test add function
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)  # Edge case: 0 + 0
        with self.assertRaises(ValueError):  # Error case: negative input
            add(-2, 3)
        with self.assertRaises(ValueError):  # Error case: negative input
            add(2, -3)
    
    # Test subtract function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    # Test multiply function
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)

    # Test divide function
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 1), 5)  # Edge case: dividing by 1
        with self.assertRaises(ValueError):  # Error case: division by zero
            divide(5, 0)

    # Test power function
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)  # Edge case: exponent is 0

    # Test modulo function
    def test_modulo(self):
        self.assertEqual(modulo(5, 3), 2)
        with self.assertRaises(ValueError):  # Error case: modulo by zero
            modulo(5, 0)

if __name__ == '__main__':
    unittest.main()
