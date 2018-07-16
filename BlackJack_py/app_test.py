import unittest

from app import foo

class TestMyApp(unittest.TestCase):
    def mean_test_name(self):
        self.assertEqual(foo("Argument"), "Expected")

if __name__ == '__main__':
    unittest.main()
