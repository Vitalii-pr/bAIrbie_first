"""Line geometry module"""


class Point:
    """Class for points in 2D space"""

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Invalid coordinates")
        self.x = x
        self.y = y

    def __eq__(self, other: "Point") -> bool:
        """Method for comparing points"""
        return self.x == other.x and self.y == other.y

class Line:
    """class for straight lines"""

    def __init__(self, p1: Point, p2: Point):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError
        if p1 == p2:
            raise ValueError("Points are identical, cannot form a line.")
        self.p1 = p1
        self.p2 = p2
        self.vertical = False
        if p1.x == p2.x:  # Check if the line is vertical
            self.vertical = True
            self.x_intercept = p1.x
        else:
            self.slope = (p2.y - p1.y) / (p2.x - p1.x)
            self.intercept = p1.y - self.slope * p1.x

    def intersect(self, other: 'Line'):
        """method for getting the point of
        intersection of two lines"""
        if not isinstance(other, Line):
            raise TypeError
        if not self.vertical and not other.vertical:
            if self.slope == other.slope and self.intercept == other.intercept:
                return self
        if self.vertical:
            if other.vertical:  # Both lines are vertical
                if self.x_intercept == other.x_intercept:
                    return self
                return None
            x = self.x_intercept
            y = other.slope * x + other.intercept
        elif other.vertical:
            x = other.x_intercept
            y = self.slope * x + self.intercept
        else:
            if self.slope == other.slope:  # Parallel lines
                return None
            x = (other.intercept - self.intercept) / (self.slope - other.slope)
            y = self.slope * x + self.intercept
        return Point(x, y)
