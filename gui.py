import os
import pygame
import pygame.locals
import sys

import config
from exception import OnExitException
from player import KeyboardPlayer


class GUI:
    def __init__(self):
        pygame.init()

        self.wm = None
        self.player = KeyboardPlayer()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.asphalt = (pygame.image.load(os.path.join("drawable/asphalt.png"))).convert()
        self.sky = (pygame.image.load(os.path.join("drawable/sky.png"))).convert()

        self.init_display()

    def set_world_model(self, wm):
        self.wm = wm

    def init_display(self):
        pygame.display.set_caption(config.WINDOW_NAME)

        # Calculate drawn area width, height, x and y
        self.daWitdh = self.screen.get_size()[0]
        self.daHeight = self.screen.get_size()[1] - (self.asphalt.get_size()[1] + self.sky.get_size()[1])
        self.daX = 0
        self.daY = self.sky.get_size()[1]
        self.daRect = pygame.Rect(self.daX,
                                  self.daY,
                                  self.daWitdh,
                                  self.daHeight)

        # Create drawn area background
        self.drawnArea = (pygame.Surface((self.daWitdh, self.daHeight))).convert()
        self.drawnArea.fill(config.BACKGROUND_COLOR)

        # Drawing images on the background
        screenY = self.screen.get_size()[1]

        self.screen.blit(self.drawnArea, (self.daX, self.daY))
        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.asphalt, (0, screenY - self.asphalt.get_size()[1]))

        pygame.display.flip()

    def draw(self):
        pygame.display.update(self.daRect)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                raise OnExitException()

        return self.player.get_next_move(self.wm)

    def close(self):
        pygame.quit()
        sys.exit()
