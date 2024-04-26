import unittest
from third_week.Polynomial.human import *

class TestPolynomial(unittest.TestCase):
    def test_init(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly = Polynomial(mono1, mono2)
        self.assertEqual(str(poly), "Polynomial: 3x**2+4x")

    def test_str(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly = Polynomial(mono1, mono2)
        self.assertEqual(str(poly), "Polynomial: 3x**2+4x")

    def test_add(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly1 = Polynomial(mono1, mono2)
        poly2 = Polynomial(Mono(2, 2), Mono(1, 0))
        result = poly1 + poly2
        self.assertEqual(str(result), "Polynomial: 5x**2+4x+1")

    def test_sub(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly1 = Polynomial(mono1, mono2)
        poly2 = Polynomial(Mono(2, 2), Mono(1, 0))
        result = poly1 - poly2
        self.assertEqual(str(result), "Polynomial: x**2+4x-1")

    def test_mul(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly1 = Polynomial(mono1, mono2)
        poly2 = Polynomial(Mono(2, 2), Mono(1, 0))
        result = poly1 * poly2
        self.assertEqual(str(result), "Polynomial: 6x**4+8x**3+3x**2+4x")

    def test_rmul(self):
        mono1 = Mono(3, 2)
        poly1 = Polynomial(mono1)
        result = 2 * poly1
        self.assertEqual(str(result), "Polynomial: 6x**2")

    def test_eq(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly1 = Polynomial(mono1, mono2)
        poly2 = Polynomial(Mono(3, 2), Mono(4, 1))
        self.assertTrue(poly1 == poly2)

    def test_eval_at(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 1)
        poly = Polynomial(mono1, mono2)
        self.assertEqual(poly.eval_at(2), 20)

if __name__ == '__main__':
    unittest.main()
