from game_of_life.board import Board
from game_of_life.cell import (
    AliveCell,
    Cell, 
    DeadCell
)
from game_of_life.position import Position


class LifeRules:
    def next_state(self, board: Board, cell: Cell) -> Cell:
        number_of_alive_neighbours = board.number_of_alive_neighbours(cell)
        
        if cell.alive() and number_of_alive_neighbours in [2,3]:
            return cell

        if not cell.alive() and number_of_alive_neighbours == 3:
            return AliveCell(cell.position())
        
        return DeadCell(cell.position())
