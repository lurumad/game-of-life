import random
from game_of_life.board import Board
from game_of_life.cell import AliveCell, DeadCell
from game_of_life.position import Position


class BoardFactory:
    def create(self, width: int, height: int) -> Board:
        cells = [[AliveCell(Position(x,y)) if random.randrange(2) else DeadCell(Position(x,y)) for y in range(height)] for x in range(width)]
        return Board(cells)
