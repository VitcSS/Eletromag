import unittest
from campo import *


class TestCampCreation(unittest.TestCase):
    def setUp(self):
        self.camp1 = Carga(3, (1, 3))
        self.camp2 = Carga(2, (5, 4))

    def test_constant_creation(self):
        self.assertEqual(3, self.camp1.load)
        self.assertEqual(2, self.camp2.load)

class TestFullCampCreation(unittest.TestCase):
    def setUp(self):
        self.camp = CampoVetorial('ar')

    def test_singleton(self):
        camp2 = CampoVetorial('etanol')
        self.assertIs(self.camp, camp2, 'Singleton funcionando')
        print(self.camp.constant)

    def test_constant(self):
        self.assertAlmostEqual(self.camp.constant, 8.995E9)

class TestVetor(unittest.TestCase):
    def setUp(self):
        position = (-3, 4)
        self.vect = Vetor(position)

    def test_module_and_position(self):
        self.assertEqual(5, self.vect.module, 'Módulo calculado corretamente')
        self.assertEqual(self.vect.x, -3)
        self.assertEqual(self.vect.y, 4)

if __name__ == '__main__':
    unittest.main()
