import unittest
from unittest import TestCase, main


class MyTests(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)


    def test_other_assertions(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)
        self.assertGreater(2, 1)
        self.assertLess(1, 2)
        self.assertIn(1, [1, 2])
        self.assertIsInstance(1, int)

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
        with self.assertRaises(TypeError):
            1 + '2'

if __name__ == '__main__':
    main()
