from physicalobject import Pendulum, Cart
from eventtype import*
import config
class WorldModel:
    def __init__(self):
        self.pendulum = Pendulum()
        self.cart = Cart()

    def update(self, event):
        G=config.GRAVITY
        N=(self.cart.mass+self.pendulum.mass)*G
        F_k=config.U_K *N
        F_smax=config.U_S *N

        if event==EventType.E_None:

            if self.cart.velocity > 0:
                a=-F_k / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity < 0 :
                    self.cart.velocity =0

            if self.cart.velocity < 0:
                a=F_k / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity > 0 :
                    self.cart.velocity =0
            self.cart.pos+=self.cart.velocity *config.Time
            if self.cart.pos > config.SPACE_WIDTH :
                self.cart.velocity =0
                self.cart.pos=config.SPACE_WIDTH
            if self.cart.pos < 0 :
                self.cart.velocity =0
                self.cart.pos =0
        if event==EventType.E_RIGHT:
            if self.cart.velocity == 0:
                if config.F_MOVEMENT > F_smax :
                    a=(config.F_MOVEMENT - F_k) / self.cart.mass
                    self.cart.velocity+=a * config.Time

            if self.cart.velocity > 0 :
                a=(config.F_MOVEMENT - F_k) / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity < 0 :
                    self.cart.velocity=0

            if self.cart.velocity < 0 :
                a=(config.F_MOVEMENT - F_k) / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity > 0 :
                    self.cart.velocity=0
            self.cart.pos+=self.cart.velocity *config.Time
            if self.cart.pos > config.SPACE_WIDTH :
                self.cart.velocity =0
                self.cart.pos=config.SPACE_WIDTH
            if self.cart.pos < 0 :
                self.cart.velocity =0
                self.cart.pos =0
        if event==EventType.E_LEFT:
            if self.cart.velocity ==0:
                if config.F_MOVEMENT >F_smax :
                    a=-(config.F_MOVEMENT-F_k) / self.cart.mass
                    self.cart.velocity+=a * config.Time

            if self.cart.velocity > 0 :
                a=-(config.F_MOVEMENT - F_k) / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity < 0 :
                    self.cart.velocity=0

            if self.cart.velocity < 0 :
                a=-(config.F_MOVEMENT - F_k) / self.cart.mass
                self.cart.velocity+=a * config.Time
                if self.cart.velocity > 0 :
                    self.cart.velocity=0
            self.cart.pos+=self.cart.velocity *config.Time
            if self.cart.pos > config.SPACE_WIDTH :
                self.cart.velocity =0
                self.cart.pos=config.SPACE_WIDTH
            if self.cart.pos < 0 :
                self.cart.velocity =0
                self.cart.pos =0

    def get_pendulum(self):
        return self.pendulum

    def get_cart(self):
        return self.cart
