from abc import ABC, abstractmethod
from dataclasses import dataclass

from game_of_life.position import Position


class Cell(ABC):
    @abstractmethod
    def alive(self) -> bool:
        pass

    @abstractmethod
    def position(self) -> Position:
        pass


class AliveCell(Cell):
    def __init__(self, position: Position) -> None:
        self._position = position

    def alive(self) -> bool:
        return True

    def position(self) -> Position:
        return self._position


class DeadCell(Cell):
    def __init__(self, position: Position) -> None:
        self._position = position

    def alive(self) -> bool:
        return False

    def position(self) -> Position:
        return self._position