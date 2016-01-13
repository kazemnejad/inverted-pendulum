from physicalobject import Pendulum, Cart


class WorldModel:
    def __init__(self):
        self.pendulum = Pendulum()
        self.cart = Cart()

    def update(self, event):
        pass
