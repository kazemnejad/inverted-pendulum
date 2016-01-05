from abc import ABCMeta, abstractmethod


class Player(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_next_move(self, wm):
        pass


