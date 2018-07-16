import unittest

from app import foo

class YearTest(unittest.TestCase):
    def mean_test_name(self):
        self.assertIs(foo("Argument"), "Expected")

if __name__ == '__main__':
    unittest.main()
