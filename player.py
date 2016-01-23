import os
import pickle
import pygame
import pygame.locals
from abc import ABCMeta, abstractmethod

import pygame.event

import config
from actiontype import ActionType


class Player(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_next_move(self):
        pass


class AIPlayer(Player):
    def __init__(self, wm):
        self.wm = wm
        self.Q = {}

        self.load_learned_data()

    def get_next_move(self):
        # get current state from world
        currentState = self.wm.get_current_state().get_discrete_state()

        # get best action for this state
        maxi = -99999
        bestAction = ActionType.ACT_NONE
        stateActions = self.Q.get(currentState, {})
        for action in stateActions:
            q = stateActions.get(action, config.DEFAULT_Q)
            if q >= maxi:
                maxi = q
                bestAction = action

        return bestAction

    def load_learned_data(self):
        if not os.path.exists(config.LEARNED_DATA["path"]):
            if not os.path.exists(config.LEARNED_DATA["dir"]):
                os.mkdir(config.LEARNED_DATA["dir"])

            open(config.LEARNED_DATA["path"], 'a').close()
        else:
            if os.stat(config.LEARNED_DATA["path"]).st_size != 0:
                with open(config.LEARNED_DATA["path"], 'rb') as f:
                    self.Q = pickle.load(f)


class KeyboardPlayer(Player):
    def __init__(self):
        self.currentEvent = ActionType.ACT_NONE

    def get_next_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return ActionType.ACT_LEFT
        if keys[pygame.K_RIGHT]:
            return ActionType.ACT_RIGHT

        return ActionType.ACT_NONE
