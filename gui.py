import os
import pygame
import pygame.locals
import sys
from math import sin, cos, radians

import config
from exception import OnExitException
from player import KeyboardPlayer, AIPlayer


class GUI:
    def __init__(self, enableAiPlayer):
        pygame.init()

        self.is_ai_player = enableAiPlayer
        self.wm = None
        if not self.is_ai_player:
            self.player = KeyboardPlayer()

        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.asphalt = (pygame.image.load(os.path.join("drawable/asphalt.png"))).convert()
        self.sky = (pygame.image.load(os.path.join("drawable/sky.png"))).convert()

        self.kX = config.SCREEN_WIDTH / config.SPACE_WIDTH
        self.kY = config.SCREEN_HEIGHT / config.SPACE_HEIGHT

        self.init_display()

    def set_world_model(self, wm):
        self.wm = wm
        if self.is_ai_player:
            self.player = AIPlayer(self.wm)

    def init_display(self):
        pygame.display.set_caption(config.WINDOW_NAME)

        # Calculate drawn area width, height, x and y
        self.daWitdh = self.screen.get_size()[0]
        self.daHeight = self.screen.get_size()[1] - (self.sky.get_size()[1])
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
        self.clean_background()
        self.draw_cart_and_pendulum()
        pygame.display.update(self.daRect)

    def draw_cart_and_pendulum(self):
        screenY = self.screen.get_size()[1]

        pendulum = self.wm.get_pendulum()
        cart = self.wm.get_cart()

        # calculate cart position
        cartX = cart.pos * self.kX - cart.drawable.get_size()[0] / 2
        cartY = screenY - self.asphalt.get_size()[1] - cart.drawable.get_size()[1]

        # calculate pendulum position
        angle = radians(pendulum.angle); cosp = cos(angle); sinp = sin(angle)

        poviotX=cart.pos*self.kX
        poviotY=cartY
        pendulumX=poviotX-100*sinp
        pendulumY=poviotY-100*cosp

        # draw the on the screen
        self.screen.blit(self.asphalt, (0, screenY - self.asphalt.get_size()[1]))
        self.screen.blit(cart.drawable, (cartX, cartY))
        pygame.draw.line(self.screen, config.ROD_COLOR, [poviotX, poviotY], [pendulumX,pendulumY], 7)
        self.screen.blit(pendulum.main_drawable, (pendulumX - pendulum.main_drawable.get_size()[0]/2, pendulumY -pendulum.main_drawable.get_size()[1]/2))

    def get_action(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                raise OnExitException()

        return self.player.get_next_move()

    def clean_background(self):
        self.screen.blit(self.drawnArea, (self.daX, self.daY))

    def close(self):
        pygame.quit()
        sys.exit()
