from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def moved(self, x: int, y: int):
        return Position(self.x + x, self.y + y)