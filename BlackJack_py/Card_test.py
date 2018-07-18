import unittest
from Card import Card

class TestCardClass(unittest.TestCase):
    def test_ace_of_spades(self):
        self.assertEqual(Card('Ace', 'Spades').get_name(), 'Ace of Spades')

    def test_queen_of_diamonds(self):
        self.assertEqual(Card('Queen', 'Diamonds').get_name(), 'Queen of Diamonds')

    def test_four_of_diamonds(self):
        self.assertEqual(Card('4', 'Diamonds').get_name(), '4 of Diamonds')

if __name__ == '__main__':
    unittest.main()
