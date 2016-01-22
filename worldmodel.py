from physicalobject import Pendulum, Cart
from eventtype import*
import config
import math
class WorldModel:
    def __init__(self):
        self.pendulum = Pendulum()
        self.cart = Cart()

    def update(self, event):
        G=config.GRAVITY
        N=(self.cart.mass+self.pendulum.mass)*G
        F_k=config.U_K *N
        F_smax=config.U_S *N
        a=0
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
            self.cart.pos+=(self.cart.velocity *config.Time)+0.5*a*(config.Time**2)
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
            self.cart.pos+=(self.cart.velocity *config.Time) + 0.5*a*(config.Time**2)
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
            self.cart.pos+=(self.cart.velocity *config.Time)+0.5*a*(config.Time**2)
            if self.cart.pos > config.SPACE_WIDTH :
                self.cart.velocity =0
                self.cart.pos=config.SPACE_WIDTH
            if self.cart.pos < 0 :
                self.cart.velocity =0
                self.cart.pos =0
        F_air=config.U_air * math.fabs(self.pendulum.w) *self.pendulum.length
        alpha_air=F_air / self.pendulum.mass
        w_air=alpha_air *config.Time
        '''
        alpha=0
        teta=math.fabs(math.radians(self.pendulum.angle))
        if a>0:
            if self.pendulum.angle >=0:
                alpha=config.GRAVITY*self.pendulum.mass*math.sin(teta)+self.pendulum.mass*a*math.cos(teta)
            if self.pendulum.angle <0:
                alpha=self.pendulum.mass*a*math.cos(teta)-config.GRAVITY*self.pendulum.mass*math.sin(teta)
        if a<0:
            a*=-1
            if self.pendulum.angle >=0:
                alpha=config.GRAVITY*self.pendulum.mass*math.sin(teta)-self.pendulum.mass*a*math.cos(teta)
            if self.pendulum.angle <0:
                alpha=-config.GRAVITY*self.pendulum.mass*math.sin(teta)-self.pendulum.mass*a*math.cos(teta)

        if self.pendulum.w>0 :
            self.pendulum.w+=alpha*config.Time -w_air
        if self.pendulum.w<0 :
            self.pendulum.w+=alpha*config.Time +w_air
        if self.pendulum.w==0 :
            self.pendulum.w=alpha*config.Time

        self.pendulum.angle+=math.degrees(self.pendulum.w*config.Time)
'''
        alpha = 3 / 2 * (G * math.sin(math.radians(self.pendulum.angle)) + a * math.cos(math.radians(self.pendulum.angle))) / 1
        dw = alpha * config.Time
        dAngle = 0.5 * alpha * config.Time ** 2 + self.pendulum.w * config.Time
        if self.pendulum.w >0 :
            self.pendulum.w += dw -w_air
        if self.pendulum.w <0 :
            self.pendulum.w += dw +w_air
        if self.pendulum.w ==0 :
            self.pendulum.w =dw
        self.pendulum.angle += math.degrees(dAngle)
    def get_pendulum(self):
        return self.pendulum

    def get_cart(self):
        return self.cart
