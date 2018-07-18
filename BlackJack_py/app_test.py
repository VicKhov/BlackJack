import unittest
from Card import Card
from app import hand_value

class TestScoring(unittest.TestCase):

    def test_scoring(self):
        self.assertEqual(hand_value([Card('Queen', 'Club'), Card('3', 'Diamond')]), ['13', 13])

if __name__ == '__main__':
    unittest.main()
