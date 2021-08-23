import numeroscomplejos as lc
import unittest
class TestCplxOperations(unittest.TestCase):
    def test_suma_complejos(self):
        suma = lc.suma_complejos((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)
        suma2 = lc.suma_complejos((2,5),(3,8))
        self.assertAlmostEqual(suma2[0], 5)
        self.assertAlmostEqual(suma2[1], 13)
    def test_producto_complejos(self):
        producto = lc.producto_complejos((2,5),(6,7))
        self.assertAlmostEqual(producto[0], -23)
        self.assertAlmostEqual(producto[1], 44)
        producto2 = lc.producto_complejos((-3,-1),(1,-2))
        self.assertAlmostEqual(producto2[0], -5)
        self.assertAlmostEqual(producto2[1], 5)
    def test_resta_complejos(self):
        resta = lc.resta_complejos((5,4),(3,2))
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], 2)
        resta2 = lc.resta_complejos((7,8),(3,5))
        self.assertAlmostEqual(resta2[0], 4)
        self.assertAlmostEqual(resta2[1], 3)
    def test_division_complejos(self):
        division = lc.division_complejos((-2,1),(1,2))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], 1)
        division2 = lc.division_complejos((0,3),(-1,-1))
        self.assertAlmostEqual(division2[0], -1.5)
        self.assertAlmostEqual(division2[1], -1.5)
    def test_modulo_complejos(self):
        modulo = lc.modulo_complejo((1,-1))
        self.assertAlmostEqual(modulo, 1.4142135623730951)
        modulo2 = lc.modulo_complejo((4,-3))
        self.assertAlmostEqual(modulo2, 5)
    def test_conjugado_complejos(self):
        conjugado = lc.conjugado_complejo((3,4))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], -4)
        conjugado2 = lc.conjugado_complejo((5, 0))
        self.assertAlmostEqual(conjugado2[0], 5)
        self.assertAlmostEqual(conjugado2[1], 0)
    def test_polartocartesian(self):
        cartesian = lc.polartocartesian((5, 60))
        self.assertAlmostEqual(cartesian[0], 2.5)
        self.assertAlmostEqual(cartesian[1], 4.330127018922193)
        cartesian2 = lc.polartocartesian((25, 45))
        self.assertAlmostEqual(cartesian2[0], 17.67766952966369)
        self.assertAlmostEqual(cartesian2[1], 17.67766952966369)
    def test_fase_complejos(self):
        fase = lc.fase_complejos((2,2))
        self.assertAlmostEqual(fase, 0.7853981633974483)
        fase2 = lc.fase_complejos((1,-1))
        self.assertAlmostEqual(fase2, -0.7853981633974483)
if __name__ == '__main__':
    unittest.main()
