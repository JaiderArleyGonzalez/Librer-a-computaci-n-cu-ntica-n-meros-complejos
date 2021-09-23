import quantum as q
from math import sqrt
import unittest
class TestStringMethods(unittest.TestCase):
    def test_canicas_coefbool(self):
        matriz_adj = [[(0, 0), (1/6, 0), (5/6, 0)],
                      [(1/3, 0), (1/2, 0), (1/6, 0)],
                      [(2/3, 0), (1/3, 0), (0, 0)]]

        vector = [[(1/2, 0)], [(0, 0)], [(1/2, 0)]]
        tiempo = 1
        click = q.Experimento_Canicas(matriz_adj, vector, tiempo)
        self.assertAlmostEqual(click, [[(0.4166666666666667, 0.0)],
        [(0.25, 0.0)], [(0.3333333333333333, 0.0)]])
if __name__ == '__main__':
    unittest.main()
    
    
