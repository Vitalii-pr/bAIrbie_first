import math
from main import Polynomial, Quadratic


def test_polynomial():
    """
    Test Polynomial Basics
    """
    # we'll use a very simple str format...


    p1 = Polynomial([5])
    assert p1.degree == 0
    assert p1.coeffs == [5]
    assert str(p1) == "Polynomial: 5"
    assert repr(p1) == 'Polynomial(coeffs=[5])'

    p2 = Polynomial([3, 5])
    assert p2.degree == 1
    assert p2.coeffs == [5, 3]
    assert str(p2) == "Polynomial: 3x+5"

    p3 = Polynomial([1, 5])
    assert str(p3) == "Polynomial: x+5"

    p4 = Polynomial([1, 2, 3])
    assert p4.degree == 2
    assert p4.coeffs == [3, 2, 1]
    assert str(p4) == "Polynomial: x**2+2x+3"
    assert repr(p4) == "Polynomial(coeffs=[1, 2, 3])"

    p5 = Polynomial([2, -3, 5])
    assert str(p5) == "Polynomial: 2x**2-3x+5"

    p6 = Polynomial([2, 0, -5])
    assert str(p6) == "Polynomial: 2x**2-5"

    p7 = Polynomial([2, 0, 0])
    assert str(p7) == "Polynomial: 2x**2"

    p8 = Polynomial([-1, 0, 0])
    assert str(p8) == "Polynomial: -x**2"

    p9 = Polynomial([0, 0, 0, 1, 2])
    assert p9.degree == 1
    assert p9.coeffs == [2, 1]
    assert str(p9) == "Polynomial: x+2"

    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert p1.eval_at(0) == 5
    assert p1.eval_at(2) == 5

    assert p2.eval_at(0) == 5
    assert p2.eval_at(2) == 11

    assert Polynomial([1, 2, 3]) == Polynomial([1, 2, 3])
    assert Polynomial([1, 2, 3]) != Polynomial([1, 2, 3, 0])
    assert Polynomial([1, 2, 3]) != Polynomial([1, 2, 0, 3])
    assert Polynomial([1, 2, 3]) != Polynomial([1, -2, 3])
    assert Polynomial([1, 2, 3]) != 42
    assert Polynomial([1, 2, 3]) != "Wahoo!"
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert Polynomial([42]) == 42


    # In fact, disregard all leading 0's in a polynomial
    assert Polynomial([0, 0, 0, 1, 2]) == Polynomial([1, 2])

    # Require that the constructor be non-destructive
    coeffs = [0, 0, 0, 1, 2]
    assert Polynomial(coeffs) == Polynomial([1, 2])
    assert coeffs == [0, 0, 0, 1, 2]

    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert Polynomial(coeffs) == Polynomial([1, 2])

    s = set()
    assert p1 not in s
    s.add(p1)
    assert p1 in s
    assert p2 not in s
    s.add(p2)
    assert p2 in s

    # multiply_by_value returns a new polynomial with all the
    # coefficients multiplied by the given value
    p10 = p4.multiply_by_value(10)
    assert isinstance(p10, Polynomial)
    assert str(p10) == 'Polynomial: 10x**2+20x+30'
    assert str(p4) == 'Polynomial: x**2+2x+3'

    # p.derivative() will return a new polynomial that is the derivative
    # of the original, using the power rule:
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    p11 = p4.derivative # 4x - 3
    assert isinstance(p11, Polynomial)
    assert str(p11) == "Polynomial: 2x+2"

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial
    p12 = p5 + p8 # (2x**2-3x+5) + (-x**2) == (x**2 - 3x + 5)
    assert isinstance(p12, Polynomial)
    assert str(p12) == "Polynomial: x**2-3x+5"
    assert str(p5) == "Polynomial: 2x**2-3x+5"

    # lastly, we can multiple polynomials together, which will multiply the
    # coefficients of two polynomials and return a new polynomial with the
    # correct coefficients.
    # More info: https://www.mathsisfun.com/algebra/polynomials-multiplying.html

    p13 = p5*p8 # (2x**2-3x+5) * (-x**2) == (-2x**4 + 3x**3 -5x**2)
    assert isinstance(p13, Polynomial)
    assert str(p13) == "Polynomial: -2x**4+3x**3-5x**2"



def test_quadratic():
    """
    Test Quadratic Class
    """
    print("Testing Quadratic class...", end="")
    # Quadratic should inherit properly from Polynomial
    q1 = Quadratic([3, 2, 1])  # 3x^2 + 2x + 1
    assert isinstance(q1, Quadratic)
    assert isinstance(q1, Polynomial)
    assert q1.eval_at(10) == 321
    assert q1.a == 3
    assert q1.b == 2
    assert q1.c == 1
    assert repr(q1) == "Quadratic(a=3, b=2, c=1)"
    assert str(q1) == "Quadratic: 3x**2+2x+1"

    # We use the quadratic formula to find the function's roots.
    # More info: https://www.mathsisfun.com/quadratic-equation-solver.html

    # the discriminant is b**2 - 4ac
    assert q1.discriminant == -8
    # use the discriminant to determine how many real roots (zeroes) exist
    assert q1.number_of_real_roots == 0
    assert not q1.get_real_roots()

    # Once again, with a double root
    q2 = Quadratic([1, -6, 9])
    assert q2.discriminant == 0
    assert q2.number_of_real_roots == 1
    [root] = q2.get_real_roots()
    assert root == 3
    assert repr(q2) == "Quadratic(a=1, b=-6, c=9)"

    # And again with two roots
    q3 = Quadratic([1, 1, -6])
    assert q3.discriminant == 25
    assert q3.number_of_real_roots == 2
    [root1, root2] = q3.get_real_roots() # smaller one first
    assert math.isclose(root1, -3) and math.isclose(root2, 2)

    # Creating a non-quadratic "Quadratic" is an error
    try:
        Quadratic([1, 2, 3, 4]) # this is cubic, should fail!
    except ValueError as err:
        message = err.args[0]
    assert message == 'Quadratic polynomial must have exactly 3 coefficients'




if __name__== '__main__':
    print('Testing Polynomial class...')
    test_polynomial()
    print('Passed!')
    print('Testing Quadratic class...')
    test_quadratic()
    print('Passed!')
