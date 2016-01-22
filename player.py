import pygame
import pygame.locals
from abc import ABCMeta, abstractmethod

import pygame.event

from actiontype import ActionType


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
        self.currentEvent = ActionType.ACT_NONE

    def get_next_move(self, wm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return ActionType.ACT_LEFT
        if keys[pygame.K_RIGHT]:
            return ActionType.ACT_RIGHT

        return ActionType.ACT_NONE
