
from game_of_life.cell import Cell
from game_of_life.position import Position


class Board:
    def __init__(self, cells: list[list[Cell]]) -> None:
        self._height = len(cells)
        self._width = len(cells[0])
        self._cells = cells

    def cells(self) -> list[list[Cell]]:
        return self._cells

    def cell_at(self, position: Position) -> Cell:
        return self._cells[position.x][position.y]

    def update(self, cell: Cell, new_cell: Cell) -> None:
        position = cell.position()
        self._cells[position.x][position.y] = new_cell

    def number_of_alive_neighbours(self, cell: Cell) -> int:
        alive_neighbours = 0
        for x in list(range(-1,2)):
            for y in list(range(-1,2)):
                position = cell.position()
                neighbour_position = position.moved(x, y)
                if not self._in_board(neighbour_position):
                    continue
                neighbour = self.cell_at(neighbour_position)
                if neighbour.alive() and cell is not neighbour:
                    alive_neighbours += 1
        return alive_neighbours

    def _in_board(self, position: Position):
        if position.x < 0 or position.x >= self._width:
            return False
        if position.y < 0 or position.y >= self._height:
            return False
        return True