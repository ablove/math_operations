# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide, exponentiate, modulo

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test valid input
        self.assertEqual(add(-2, 3), "Warning: Negative numbers are not allowed.")  # Test negative input
        self.assertEqual(add(2, -3), "Warning: Negative numbers are not allowed.")  # Test negative input
        self.assertEqual(add(-2, -3), "Warning: Negative numbers are not allowed.")  # Test negative input

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(6, 0), "Error: Cannot divide by zero.")

    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 3), 8)

    def test_modulo(self):
        self.assertEqual(modulo(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
