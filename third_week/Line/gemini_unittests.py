import unittest

from unittest import TestCase
from test import Point, Line

class TestPoint(TestCase):
    def test_init_valid(self):
        point = Point(3, 4.2)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4.2)

    def test_init_invalid_type(self):
        with self.assertRaises(TypeError):
            Point("hello", 2)

    def test_eq(self):
        p1 = Point(1, 1)
        p2 = Point(1, 1)
        p3 = Point(2, 3)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

class TestLine(TestCase):
    def test_init_valid(self):
        p1 = Point(1, 2)
        p2 = Point(3, 5)
        line = Line(p1, p2)
        self.assertEqual(line.p1, p1)
        self.assertEqual(line.p2, p2)
        self.assertAlmostEqual(line.slope, 1.5)
        self.assertAlmostEqual(line.intercept, 0.5)

    def test_init_invalid_type(self):
        with self.assertRaises(TypeError):
            Line(1, Point(3, 4))

    def test_init_identical_points(self):
        with self.assertRaises(ValueError):
            Line(Point(2, 2), Point(2, 2))

    def test_intersect_parallel(self):
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(0, 2), Point(2, 4))
        self.assertIsNone(line1.intersect(line2))

    def test_intersect_coincident(self):
        line1 = Line(Point(1, 1), Point(4, 4))
        line2 = Line(Point(-2, -2), Point(1, 1))
        line_check = line1.intersect(line2)
        self.assertEqual((line_check.slope, line_check.intercept),\
                        (line1.slope, line1.intercept))

    def test_intersect_not_a_line(self):
        line1 = Line(Point(1, 1), Point(4, 4))
        with self.assertRaises(TypeError):
            line1.intersect('Hello')

    def test_intersect_vertical_and_nonvertical(self):
        line1 = Line(Point(2, 0), Point(2, 3))
        line2 = Line(Point(0, 1), Point(4, 3))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, Point(2, 2))

    def test_intersect_nonvertical_and_vertical(self):
        line1 = Line(Point(2, 0), Point(2, 3))
        line2 = Line(Point(0, 1), Point(4, 3))
        intersection = line2.intersect(line1)
        self.assertEqual(intersection, Point(2, 2))

    def test_intersect_paralel_vertical(self):
        line1 = Line(Point(2, 0), Point(2, 3))
        line2 = Line(Point(4, 1), Point(4, 3))
        intersection = line2.intersect(line1)
        self.assertIsNone(intersection)

    def test_intersect_two_vertical(self):
        line1 = Line(Point(-1, 0), Point(-1, 4))
        line2 = Line(Point(-1, 2), Point(-1, 5))
        self.assertEqual(line1.intersect(line2), line1)  

    def test_intersect_general_case(self):
        line1 = Line(Point(5, 1), Point(1, 5))
        line2 = Line(Point(2, -1), Point(5, 11))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, Point(3, 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
