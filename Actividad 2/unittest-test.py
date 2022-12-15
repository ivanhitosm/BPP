import unittest
from Script import suma, resta, multiplicar, division,exponente

class TestCalculator(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(-1, -1), -2)
        self.assertEqual(suma(1, -1), 0)

    def test_resta(self):
        self.assertEqual(resta(1, 2), -1)
        self.assertEqual(resta(-1, -1), 0)
        self.assertEqual(resta(1, -1), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(1, 2), 2)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(1, 0), 0)

    def test_division(self):
        self.assertEqual(division(1, 2), 0.5)
        self.assertEqual(division(-1, -1), 1)
        self.assertRaises(ValueError, division, 1, 0)
        
    def test_exponente(self):
        self.assertEqual(exponente(1, 2), 2)
        self.assertEqual(exponente(-1, -1), 1)
        self.assertEqual(exponente(1, 0), 1)

if __name__ == '__main__':
    unittest.main()
