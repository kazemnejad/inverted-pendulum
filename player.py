import pygame
import pygame.event
import pygame.locals
from abc import ABCMeta, abstractmethod

from eventtype import EventType


class Player(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_next_move(self, wm):
        pass


class AIPlayer(Player):
    def __init__(self):
        pass

    def get_next_move(self, wm):
        pass


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
