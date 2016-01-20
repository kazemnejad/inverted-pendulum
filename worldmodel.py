from physicalobject import Pendulum, Cart


class WorldModel:
    def __init__(self):
        self.pendulum = Pendulum()
        self.cart = Cart()

    def update(self, event):
        pass

    def get_pendulum(self):
        return self.pendulum

    def get_cart(self):
        return self.cart
