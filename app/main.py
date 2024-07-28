from __future__ import annotations


class Vector:

    def __init__(self, abscissa: int | float, ordinate: int | float) -> None:
        self.x = round(abscissa, 2)
        self.y = round(ordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
