from game_of_life.board import Board
from game_of_life.cell import Cell
from game_of_life.life_rules import LifeRules


class Game:
    def __init__(self, board: Board, rules: LifeRules) -> None:
        self.board = board
        self.rules = rules

    def next_generation(self):
        for cells in self.board.cells():
            for cell in cells:
                new_cell = self.rules.next_state(self.board, cell)
                self.board.update(cell, new_cell)

    def cells(self) -> list[list[Cell]]:
        return self.board.cells()

