import unittest
from fibonacci_lru_cache import fibonacci


class TestFibonacci_LRU(unittest.TestCase):
    def test_valids(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)

    def test_invalid(self):
        self.assertRaises(TypeError, fibonacci, 'a')
        self.assertRaises(TypeError, fibonacci, 'hello')
        self.assertRaises(TypeError, fibonacci, -1)
        self.assertRaises(TypeError, fibonacci, 2.9)
        
