from __future__ import annotations


class Vector:

    def __init__(self, abscissa: int | float, ordinate: int | float) -> None:
        self.x = round(abscissa, 2)
        self.y = round(ordinate, 2)
