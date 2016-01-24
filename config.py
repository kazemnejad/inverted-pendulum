LEARNED_DATA = {
    "path": 'learned_data/ld.pkl',
    "dir": "learned_data",
    "backup_prefix": "ld.pkl.back"
}

PENDULUM = {
    "mass": 1,
    "length": 0.8,
    "main_drawable": "drawable/pendulum.png",
}
CART = {
    "mass": 50,
    "height": 0.56,
    "drawable": "drawable/cart.png"
}

SCREEN_WIDTH = 1076
SCREEN_HEIGHT = 720
DEGREE_STEP = 3
WINDOW_NAME = "Inverted Pendulum"
BACKGROUND_COLOR = (5, 187, 246)
ROD_COLOR = (108, 0, 255)
DEFAULT_Q = 0

Q_GAMMA = 0.9
Q_ALPHA = 0.5
NEAR_WALL_REPEATS = 100
SUCCESS_REPEATS = 3
POINTLESS_REPEATS = 170

SPACE_WIDTH = 10.76
SPACE_HEIGHT = 7.2

GRAVITY = 9.8
F_MOVEMENT = 2000
U_S = 0.5
U_K = 0.3
Time = 0.001
U_air = 0.1
