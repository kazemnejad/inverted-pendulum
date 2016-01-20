import logging

from exception import OnExitException
from gui import GUI
from worldmodel import WorldModel


class Engine(object):
    def __init__(self):
        logging.basicConfig(filename='app.log',level=logging.DEBUG)
        self.gui = GUI()
        self.wm = WorldModel()
        self.gui.set_world_model(self.wm)
        self.running = True

    def run(self):
        while True:
            self.gui.draw()

            event = None
            try:
                event = self.gui.get_events()
            except OnExitException:
                self.running = False
                self.gui.close()

            self.wm.update(event)
