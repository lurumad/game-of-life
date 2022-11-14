import sys
import time
import pygame
from game_of_life.board_factory import BoardFactory
from game_of_life.game import Game
from game_of_life.life_rules import LifeRules


def start():
    width = 50
    height = 50
    board_factory = BoardFactory()
    board = board_factory.create(width, height)
    rules = LifeRules()
    game = Game(board, rules)
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    while True:
        if pygame.QUIT in [e.type for e in pygame.event.get()]:
            sys.exit(0)

        screen.fill((0, 0, 0))
        draw_grid(screen, game, width, height)
        game.next_generation()
        pygame.display.flip()
        time.sleep(0.5)

def draw_grid(screen: pygame.Surface, game: Game, width: int, height: int) -> None:
    cell_width = screen.get_width() / width
    cell_height = screen.get_height() / height
    border_size = 2

    for cells in game.cells():
        for cell in cells:
            color = (255, 0, 0) if cell.alive() else (0, 0, 255)
            position = cell.position()
            x = position.x * cell_width + border_size
            y = position.y * cell_height + border_size
            rect_width = cell_width - border_size
            rect_height = cell_height - border_size
            pygame.draw.rect(screen, color, (x, y, rect_width, rect_height))


