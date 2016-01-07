import pygame
import pygame.locals
import sys

import config
from exception import OnExitException
from player import KeyboardPlayer


class GUI:
    def __init__(self, wm):
        pygame.init()

        self.wm = wm
        self.player = KeyboardPlayer()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption(config.WINDOW_NAME)
        pygame.display.flip()

    def draw(self, wm):
        pass

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                raise OnExitException()

        return self.player.get_next_move(self.wm)

    def close(self):
        pygame.quit()
        sys.exit()
