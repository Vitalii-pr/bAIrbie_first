import unittest
from main import Polynomial, Quadratic


class TestPolynomial(unittest.TestCase):

    def test_polynomial_basics(self):
        # Test Polynomial Basics
        p1 = Polynomial([5])
        self.assertEqual(p1.degree, 0)
        self.assertEqual(p1.coeffs, [5])
        self.assertEqual(str(p1), "Polynomial: 5")
        self.assertEqual(repr(p1), 'Polynomial(coeffs=[5])')

        p2 = Polynomial([3, 5])
        self.assertEqual(p2.degree, 1)
        self.assertEqual(p2.coeffs, [5, 3])
        self.assertEqual(str(p2), "Polynomial: 3x+5")

        p3 = Polynomial([1, 5])
        self.assertEqual(str(p3), "Polynomial: x+5")

        p4 = Polynomial([1, 2, 3])
        self.assertEqual(p4.degree, 2)
        self.assertEqual(p4.coeffs, [3, 2, 1])
        self.assertEqual(str(p4), "Polynomial: x**2+2x+3")
        self.assertEqual(repr(p4), "Polynomial(coeffs=[1, 2, 3])")

        p5 = Polynomial([2, -3, 5])
        self.assertEqual(str(p5), "Polynomial: 2x**2-3x+5")

        p6 = Polynomial([2, 0, -5])
        self.assertEqual(str(p6), "Polynomial: 2x**2-5")

        p7 = Polynomial([2, 0, 0])
        self.assertEqual(str(p7), "Polynomial: 2x**2")

        p8 = Polynomial([-1, 0, 0])
        self.assertEqual(str(p8), "Polynomial: -x**2")

        p9 = Polynomial([0, 0, 0, 1, 2])
        self.assertEqual(p9.degree, 1)
        self.assertEqual(p9.coeffs, [2, 1])
        self.assertEqual(str(p9), "Polynomial: x+2")

    def test_polynomial_eval_at(self):
        # Test eval_at
        p1 = Polynomial([5])
        self.assertEqual(p1.eval_at(0), 5)
        self.assertEqual(p1.eval_at(2), 5)

        p2 = Polynomial([3, 5])
        self.assertEqual(p2.eval_at(0), 5)
        self.assertEqual(p2.eval_at(2), 11)

    def test_polynomial_equality(self):
        # Test equality
        self.assertEqual(Polynomial([1, 2, 3]), Polynomial([1, 2, 3]))
        self.assertNotEqual(Polynomial([1, 2, 3]), Polynomial([1, 2, 3, 0]))
        self.assertNotEqual(Polynomial([1, 2, 3]), Polynomial([1, 2, 0, 3]))
        self.assertNotEqual(Polynomial([1, 2, 3]), Polynomial([1, -2, 3]))
        self.assertNotEqual(Polynomial([1, 2, 3]), 42)
        self.assertNotEqual(Polynomial([1, 2, 3]), "Wahoo!")
        self.assertEqual(Polynomial([42]), 42)

    def test_polynomial_constructor(self):
        # Test constructor behavior
        coeffs = [0, 0, 0, 1, 2]
        self.assertEqual(Polynomial(coeffs), Polynomial([1, 2]))
        self.assertEqual(coeffs, [0, 0, 0, 1, 2])

        coeffs = (0, 0, 0, 1, 2)
        self.assertEqual(Polynomial(coeffs), Polynomial([1, 2]))

    def test_polynomial_membership(self):
        # Test membership
        s = set()
        p1 = Polynomial([5])
        p2 = Polynomial([3, 5])
        self.assertNotIn(p1, s)
        s.add(p1)
        self.assertIn(p1, s)
        self.assertNotIn(p2, s)
        s.add(p2)
        self.assertIn(p2, s)

    def test_polynomial_multiply_derivative(self):
        # Test multiply_by_value and derivative
        p4 = Polynomial([1, 2, 3])
        p10 = p4.multiply_by_value(10)
        self.assertIsInstance(p10, Polynomial)
        self.assertEqual(str(p10), 'Polynomial: 10x**2+20x+30')
        self.assertEqual(str(p4), 'Polynomial: x**2+2x+3')

        p11 = p4.derivative
        self.assertIsInstance(p11, Polynomial)
        self.assertEqual(str(p11), "Polynomial: 2x+2")

    def test_polynomial_add_multiply(self):
        # Test addition and multiplication of polynomials
        p5 = Polynomial([2, -3, 5])
        p8 = Polynomial([-1, 0, 0])
        p12 = p5 + p8
        self.assertIsInstance(p12, Polynomial)
        self.assertEqual(str(p12), "Polynomial: x**2-3x+5")
        self.assertEqual(str(p5), "Polynomial: 2x**2-3x+5")

        p13 = p5 * p8
        self.assertIsInstance(p13, Polynomial)
        self.assertEqual(str(p13), "Polynomial: -2x**4+3x**3-5x**2")

    def test_polynomial_zero_degree(self):
        # Test polynomial of degree 0
        p1 = Polynomial([0])
        self.assertEqual(p1.degree, 0)
        self.assertEqual(p1.coeffs, [0])
        self.assertEqual(str(p1), "Polynomial: 0")
        self.assertEqual(p1.eval_at(10), 0)

    def test_polynomial_remove_leading_zeros(self):
        # Test removing leading zeros in polynomial
        p1 = Polynomial([0, 0, 0, 1, 2])
        self.assertEqual(p1.degree, 1)
        self.assertEqual(p1.coeffs, [2, 1])
        self.assertEqual(str(p1), "Polynomial: x+2")


class TestQuadratic(unittest.TestCase):

    def test_quadratic_basics(self):
        # Test Quadratic Basics
        q1 = Quadratic([3, 2, 1])  # 3x^2 + 2x + 1
        self.assertIsInstance(q1, Quadratic)
        self.assertIsInstance(q1, Polynomial)
        self.assertEqual(q1.eval_at(10), 321)
        self.assertEqual(q1.a, 3)
        self.assertEqual(q1.b, 2)
        self.assertEqual(q1.c, 1)
        self.assertEqual(repr(q1), "Quadratic(a=3, b=2, c=1)")
        self.assertEqual(str(q1), "Quadratic: 3x**2+2x+1")

    def test_quadratic_roots(self):
        # Test roots computation
        q2 = Quadratic([1, -6, 9])
        self.assertEqual(q2.discriminant, 0)
        self.assertEqual(q2.number_of_real_roots, 1)
        [root] = q2.get_real_roots()
        self.assertAlmostEqual(root, 3)

        q3 = Quadratic([1, 1, -6])
        self.assertEqual(q3.discriminant, 25)
        self.assertEqual(q3.number_of_real_roots, 2)
        [root1, root2] = q3.get_real_roots()
        self.assertAlmostEqual(root1, -3)
        self.assertAlmostEqual(root2, 2)

    def test_quadratic_no_real_roots(self):
        # Test quadratic with no real roots
        q1 = Quadratic([1, 1, 1])
        self.assertEqual(q1.discriminant, -3)
        self.assertEqual(q1.number_of_real_roots, 0)
        self.assertFalse(q1.get_real_roots())

    def test_quadratic_duplicate_root(self):
        # Test quadratic with a duplicate root
        q1 = Quadratic([1, -6, 9])
        self.assertEqual(q1.discriminant, 0)
        self.assertEqual(q1.number_of_real_roots, 1)
        [root] = q1.get_real_roots()
        self.assertAlmostEqual(root, 3)