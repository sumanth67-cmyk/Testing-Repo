import unittest
from app import add_numbers, divide_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        # This will fail because 5 + 5 will return 0
        self.assertEqual(add_numbers(5, 5), 10)

    def test_divide_numbers(self):
        # This will pass
        self.assertEqual(divide_numbers(10, 2), 5)
        
    def test_divide_by_zero(self):
        # This will error out because the app doesn't handle zero division
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()
