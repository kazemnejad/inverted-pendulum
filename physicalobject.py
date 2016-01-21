import os
import pygame

import config


class Pendulum:
    def __init__(self):
        self.mass = config.PENDULUM["mass"]
        self.length = config.PENDULUM["length"]
        self.main_drawable = (pygame.image.load(os.path.join(config.PENDULUM["main_drawable"]))).convert()
        self.rod_drawable = (pygame.image.load(os.path.join(config.PENDULUM["handle_drawable"]))).convert()
        self.angle = 0
        self.w = 0


class Cart:
    def __init__(self):
        self.mass = config.CART["mass"]
        self.height = config.CART["height"]
        self.drawable = (pygame.image.load(os.path.join(config.CART["drawable"]))).convert()
        self.pos =  0 #config.SPACE_WIDTH / 2
        self.velocity=0
