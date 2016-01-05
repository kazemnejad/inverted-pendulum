import pygame
import pygame.locals, pygame.event
from EventType import EventType

from Player import Player


class KeyboardPlayer(Player):
    def __init__(self):
        self.currentEvent = EventType.E_None

    def get_next_move(self, wm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return EventType.E_LEFT
        if keys[pygame.K_RIGHT]:
            return EventType.E_RIGHT

        return EventType.E_None


