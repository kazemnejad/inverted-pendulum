from exception import OnExitException
from gui import GUI
from worldmodel import WorldModel


class Engine(object):
    def __init__(self):
        self.wm = WorldModel()
        self.gui = GUI(self.wm)
        self.running = True

    def run(self):
        while True:
            self.gui.draw(self.wm)

            event = None
            try:
                event = self.gui.get_events()
            except OnExitException:
                self.running = False
                self.gui.close()

            self.wm.update(event)
