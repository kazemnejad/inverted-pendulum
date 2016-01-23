import os
import pygame

import config


class Pendulum:
    def __init__(self):
        self.mass = config.PENDULUM["mass"]
        self.length = config.PENDULUM["length"]
        try:
            self.main_drawable = (pygame.image.load(os.path.join(config.PENDULUM["main_drawable"]))).convert()
            self.rod_drawable = (pygame.image.load(os.path.join(config.PENDULUM["handle_drawable"]))).convert_alpha()
        except Exception:
            self.main_drawable = None
            self.rod_drawable = None

        self.angle = 0.0
        self.w = 0.0


class Cart:
    def __init__(self):
        self.mass = config.CART["mass"]
        self.height = config.CART["height"]
        try:
            self.drawable = (pygame.image.load(os.path.join(config.CART["drawable"]))).convert()
        except Exception:
            self.drawable = None

        self.pos = config.SPACE_WIDTH / 2
        self.velocity = 0
