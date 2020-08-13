import unittest
from campo import *


class TestCampCreation(unittest.TestCase):
    def setUp(self):
        self.camp1 = Campo(3, (1, 3))
        self.camp2 = Campo(2, (5, 4))

    def test_constant_creation(self):
        self.assertEqual(3, self.camp1.load)
        self.assertEqual(2, self.camp2.load)

if __name__ == '__main__':
    unittest.main()
