import unittest
from calculator import sum,multi,resta,div,modulo,conjugado,cartetopolar,polartocarte,fase
class Testcalculator(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 2],[0, 5]), (2, 7))
        self.assertEqual(sum([-5, 8],[2, 1]), (-3, 9))
    def test_multi(self):
        self.assertEqual(multi([5, 4],[0, 0]), (0, 0))
        self.assertEqual(multi([5, 4],[1, 0]), (5, 4))
    def test_resta(self):
        self.assertEqual(resta([3, -2],[0, 0]), (3, -2))
        self.assertEqual(resta([-8, 5],[3, 2]), (-11, 3))
    def test_div(self):
        self.assertEqual(div([0, -3],[-1, -1]), (1.5, 1.5))
        self.assertEqual(div([0, 0],[0, -1]), (0, 0))
    def test_modulo(self):
        self.assertEqual(modulo([4, -3]),5.0)
        self.assertEqual(modulo([4, 3]),5.0)
    def test_conjugado(self):
        self.assertEqual(conjugado([4, 3]), (4, -3))
        self.assertEqual(conjugado([4,-3]),(4, 3))
    def test_cartetopolar(self):
        self.assertEqual(cartetopolar([2, 2]),(45.022084580792125, 1.5394732415488905))
        self.assertEqual(cartetopolar([-1, 2]),(60.10316464213844, 1.5121968273544364))
    def test_polartocarte(self):
        self.assertEqual(polartocarte([1.41, 45]),(4.589293016703022, -1.0707092446824535))
        self.assertEqual(polartocarte([3.52, 60]), (3.141592653589793, 0.0))
    def test_fase(self):
        self.assertEqual(fase([5, 5]), 0.7853981633974483)
        self.assertEqual(fase([1, 0]), 0.0)
    
if __name__ == '__main__':
    unittest.main()