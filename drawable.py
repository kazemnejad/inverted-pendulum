import pygame


class Drawable(object):
    def __init__(self, filename):
        self.filename = filename
        self.surface = None

    def load(self):
        if self.surface is not None:
            self.surface = pygame.image.load(self.filename)

    def get_surface(self):
        return self.surface

    def set_surface(self, surface):
        self.surface = surface
