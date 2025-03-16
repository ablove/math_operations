# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide, exponentiate, modulo

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 8), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 0), "Cannot divide by zero")

    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(5, 0), 1)

    def test_modulo(self):
        self.assertEqual(modulo(5, 2), 1)
        self.assertEqual(modulo(10, 3), 1)

if __name__ == "__main__":
    unittest.main()
