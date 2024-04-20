class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        """Adds two vectors and returns the resulting vector"""
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Vector(result_x, result_y)

    def __repr__(self):
        """Creates a string representation of the vector"""
        return f"Vector({self.x}, {self.y})"
