import config


class State:
    def __init__(self, angle, pos, pendulum_w=0, cart_vel=0):
        self.angle = angle
        self.pos = pos
        self.w = pendulum_w
        self.vel = cart_vel

    def get_discrete_state(self):
        pos = int(self.pos)

        angle = self.angle
        if self.angle >= 360:
            angle = self.angle % 360
        if self.angle <= -360:
            angle = self.angle % -360
        angle = angle if angle >= 0 else 360 - abs(angle)

        return State(angle // config.DEGREE_STEP, pos)

    def __str__(self):
        return "pos: " + str(self.pos) \
               + ", angle: " + str(self.angle) \
               + ", vel: " + str(self.vel) \
               + ", w: " + str(self.w)

    def __eq__(self, other):
        return (self.angle, self.pos) == (other.angle, other.pos)

    def __hash__(self):
        return hash((self.angle, self.pos))
