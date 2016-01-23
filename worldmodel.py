import math
import random

import config
from actiontype import *
from physicalobject import Pendulum, Cart
from qlearning import State


class WorldModel:
    def __init__(self):
        self.pendulum = Pendulum()
        self.cart = Cart()

        self.reset_with_random_state()

    def update(self, action):
        # calculate next state
        nextState = self.compute_next_state(action)

        # update current state
        self.cart.pos = nextState.pos
        self.cart.velocity = nextState.vel
        self.pendulum.angle = nextState.angle
        self.pendulum.w = nextState.w

    def reset_with_random_state(self):
        # reset position & angle
        self.cart.pos = random.uniform(40.0 / 100 * config.SPACE_WIDTH, 60.0 / 100 * config.SPACE_WIDTH)
        self.pendulum.angle = random.uniform(-30.0, 30.0)
        while self.pendulum.angle == 0:
            self.pendulum.angle = random.randint(-30, 30)

        # reset W & velocity
        self.cart.velocity = 0
        self.pendulum.w = 0

    def compute_next_state(self, action):
        G = config.GRAVITY
        N = (self.cart.mass + self.pendulum.mass) * G
        F_k = config.U_K * N
        F_smax = config.U_S * N
        a = 0

        # current state
        cart_velocity = self.cart.velocity
        cart_pos = self.cart.pos
        pendulum_angle = self.pendulum.angle
        pendulum_w = self.pendulum.w

        if action == ActionType.ACT_NONE:
            if cart_velocity > 0:
                a = -F_k / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity < 0:
                    cart_velocity = 0

            if cart_velocity < 0:
                a = F_k / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity > 0:
                    cart_velocity = 0
            cart_pos += (cart_velocity * config.Time) + 0.5 * a * (config.Time ** 2)
            if cart_pos > config.SPACE_WIDTH:
                cart_velocity = 0
                cart_pos = config.SPACE_WIDTH
            if cart_pos < 0:
                cart_velocity = 0
                cart_pos = 0

        if action == ActionType.ACT_RIGHT:
            if cart_velocity == 0:
                if config.F_MOVEMENT > F_smax:
                    a = (config.F_MOVEMENT - F_k) / self.cart.mass
                    cart_velocity += a * config.Time
            if cart_velocity > 0:
                a = (config.F_MOVEMENT - F_k) / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity < 0:
                    cart_velocity = 0
            if cart_velocity < 0:
                a = (config.F_MOVEMENT - F_k) / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity > 0:
                    cart_velocity = 0
            cart_pos += (cart_velocity * config.Time) + 0.5 * a * (config.Time ** 2)
            if cart_pos > config.SPACE_WIDTH:
                cart_velocity = 0
                cart_pos = config.SPACE_WIDTH
            if cart_pos < 0:
                cart_velocity = 0
                cart_pos = 0

        if action == ActionType.ACT_LEFT:
            if cart_velocity == 0:
                if config.F_MOVEMENT > F_smax:
                    a = -(config.F_MOVEMENT - F_k) / self.cart.mass
                    cart_velocity += a * config.Time
            if cart_velocity > 0:
                a = -(config.F_MOVEMENT - F_k) / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity < 0:
                    cart_velocity = 0
            if cart_velocity < 0:
                a = -(config.F_MOVEMENT - F_k) / self.cart.mass
                cart_velocity += a * config.Time
                if cart_velocity > 0:
                    cart_velocity = 0
            cart_pos += (cart_velocity * config.Time) + 0.5 * a * (config.Time ** 2)
            if cart_pos > config.SPACE_WIDTH:
                cart_velocity = 0
                cart_pos = config.SPACE_WIDTH
            if cart_pos < 0:
                cart_velocity = 0
                cart_pos = 0

        F_air = config.U_air * math.fabs(pendulum_w) * self.pendulum.length
        alpha_air = F_air / self.pendulum.mass
        w_air = alpha_air * config.Time
        alpha = 3 / 2 * (
            G * math.sin(math.radians(pendulum_angle)) + a * math.cos(math.radians(pendulum_angle))) / 1
        dw = alpha * config.Time
        dAngle = 0.5 * alpha * config.Time ** 2 + pendulum_w * config.Time
        if pendulum_w > 0:
            pendulum_w += dw - w_air
        if pendulum_w < 0:
            pendulum_w += dw + w_air
        if pendulum_w == 0:
            pendulum_w = dw
        pendulum_angle += math.degrees(dAngle)

        return State(pendulum_angle, cart_pos, pendulum_w, cart_velocity)

    def get_current_state(self):
        return State(self.pendulum.angle, self.cart.pos, self.pendulum.w, self.cart.velocity)

    def get_pendulum(self):
        return self.pendulum

    def get_cart(self):
        return self.cart
