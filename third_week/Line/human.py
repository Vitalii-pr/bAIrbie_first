"""line geometry module"""

class Point:
    """class for points in 2 dimentional space"""

    def __init__(self, x: float, y: float) -> None:
        if not type(x) in (int, float) or not type(y) in (int, float):
            raise TypeError
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point'):
        """method for comparing points"""
        return self.x == other.x and self.y == other.y

class Line:
    """class for straight lines"""

    def __init__(self, p1: Point, p2: Point):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError
        if p1 == p2:
            raise ValueError
        self.p1 = p1
        self.p2 = p2
        try:
            self.b_coef = (p2.y - p1.y) / (p2.x - p1.x)
        except ZeroDivisionError:
            self.b_coef = 0
        self.c_coef = p1.y - self.b_coef * p1.x

    def intersect(self, other: 'Line'):
        """method for getting the point of
        intersection of two lines"""
        if not isinstance(other, Line):
            raise TypeError
        if self.b_coef == other.b_coef and self.c_coef == other.c_coef:
            return self  # the lines the same
        if self.b_coef == other.b_coef and self.c_coef != other.c_coef:
            return None  # the lines are parallel
        x = (other.c_coef - self.c_coef)/(self.b_coef - other.b_coef)
        y = self.b_coef * x + self.c_coef
        return Point(x, y)
