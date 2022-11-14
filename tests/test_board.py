import pytest
from game_of_life.board import Board
from game_of_life.cell import (
    AliveCell, 
    DeadCell
)
from game_of_life.position import Position


class TestBoard:
    def test_should_return_zero_when_there_are_not_alive_neighbours(self):
        cell = AliveCell(Position(1, 1))
        initial = [
            [DeadCell(Position(0, 0)),DeadCell(Position(0, 1)),DeadCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert board.number_of_alive_neighbours(cell) == 0

    def test_should_return_the_number_of_alive_neighbours(self):
        cell = AliveCell(Position(1, 1))
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [AliveCell(Position(1, 0)),cell,AliveCell(Position(1, 2))],
            [AliveCell(Position(2, 0)),AliveCell(Position(2, 1)),AliveCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert board.number_of_alive_neighbours(cell) == 8

    def test_should_return_the_cell_at_a_given_position(self):
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [AliveCell(Position(1, 0)),AliveCell(Position(1, 1)),AliveCell(Position(1, 2))],
            [AliveCell(Position(2, 0)),AliveCell(Position(2, 1)),AliveCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert board.cell_at(Position(1, 1)).alive() == True

    def test_update_cell_at_a_given_position(self):
        alive_cell = AliveCell(Position(1, 1))
        dead_cell = DeadCell(Position(1, 1))
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [AliveCell(Position(1, 0)),alive_cell,AliveCell(Position(1, 2))],
            [AliveCell(Position(2, 0)),AliveCell(Position(2, 1)),AliveCell(Position(2, 2))]
        ]
        board = Board(initial)
        board.update(alive_cell, dead_cell)
        assert board.cell_at(Position(1, 1)).alive() == False

