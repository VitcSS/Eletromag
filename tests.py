import unittest
from campo import *


class TestCampCreation(unittest.TestCase):
    def setUp(self):
        self.camp1 = Campo(3, (1, 3))
        self.camp2 = Campo(2, (5, 4), constant='ar')

    def test_constant_creation(self):
        self.assertAlmostEqual(8.995E9, self.camp2.constant, 'Campo definido')
        self.assertAlmostEqual(9E9, self.camp1.constant, 'Campo não definido')

if __name__ == '__main__':
    unittest.main()
