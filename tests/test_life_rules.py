import pytest
from game_of_life.board import Board
from game_of_life.cell import (
    AliveCell, 
    DeadCell
)
from game_of_life.life_rules import LifeRules
from game_of_life.position import Position


class TestLifeRules:
    def test_any_live_cell_with_less_than_two_live_neighbours_dead(self):
        alive_cell = AliveCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),DeadCell(Position(0, 1)),DeadCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),alive_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board, alive_cell).alive() == False
    
    def test_any_live_cell_with_more_than_three_live_neighbours_dead(self):
        alive_cell = AliveCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [AliveCell(Position(1, 0)),alive_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board, alive_cell).alive() == False

    def test_any_dead_cell_with_three_live_neighbours_becomes_a_live_cell(self):
        dead_cell = DeadCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),dead_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board,  dead_cell).alive() == True

    def test_any_live_cell_with_two_live_neighbours_survives(self):
        alive_cell = AliveCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),DeadCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),alive_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board, alive_cell).alive() == True

    def test_any_live_cell_with_three_neighbours_survives(self):
        alive_cell = AliveCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),AliveCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),alive_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board, alive_cell).alive() == True

    def test_all_other_dead_cell_without_three_live_neighbours_stay_dead(self):
        dead_cell = DeadCell(Position(1, 1))
        lifeRules = LifeRules()
        initial = [
            [AliveCell(Position(0, 0)),AliveCell(Position(0, 1)),DeadCell(Position(0, 2))],
            [DeadCell(Position(1, 0)),dead_cell,DeadCell(Position(1, 2))],
            [DeadCell(Position(2, 0)),DeadCell(Position(2, 1)),DeadCell(Position(2, 2))]
        ]
        board = Board(initial)
        assert lifeRules.next_state(board, dead_cell).alive() == False