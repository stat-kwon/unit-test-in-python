"""
The unittest module provides a rich set of tools for constructing and running tests.
 - a small subset of the tools suffice to meet the needs of most users.
"""

# Example1 : A short script to test three string methods.
import unittest


class TestStringMethods(unittest.TestCase):  # subclassing unittest.TestCase

    # The three individual tests are defined with methods whose names start with the letters test.
    # test_ naming informs the test runner about which methods represent tests
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# unittest.main() provides a CLI to the test script.
if __name__ == '__main__':
    unittest.main()
