import os
import pickle
import random

import config
from actiontype import ActionType
from exception import OnExitException
from gui import GUI
from worldmodel import WorldModel


class Engine(object):
    def __init__(self):
        self.gui = GUI()
        self.wm = WorldModel()
        self.gui.set_world_model(self.wm)
        self.running = True

    def run(self):
        while True:
            self.gui.draw()

            action = None
            try:
                action = self.gui.get_action()
            except OnExitException:
                self.running = False
                self.gui.close()

            self.wm.update(action)


class LeaningEngine:
    def __init__(self, episodeNum):
        self.episode_num = episodeNum
        self.gui = GUI()
        self.wm = WorldModel()
        self.gui.set_world_model(self.wm)

        self.Q = {}
        self.num_of_is_near_wall = 0
        self.num_of_success_repeat = 0

        self.load_learned_data()

        # for key in self.Q.keys():
        #     print "(" +str(key[0].angle * config.DEGREE_STEP) + ", " + str(key[0].pos) + ") action: " + str(key[1]) + " : "
        #     # print self.Q.keys()

    def run(self):
        for i in range(self.episode_num):
            self.log_start_episode(i + 1)

            # init with random state
            self.wm.reset_with_random_state()

            while True:
                self.gui.draw()
                # get current world state
                currentState = self.wm.get_current_state().get_discrete_state()

                # select a random action
                randomAction = random.choice(ActionType.ALL_ACTIONS)

                # compute next world state but not updating it
                nextState = self.wm.compute_next_state(randomAction).get_discrete_state()

                # calculated reward base on current state
                reward = self.calculate_reward()

                # get max of Q for the next state and all possible action
                maxQ = max([self.Q.get((nextState, action), config.DEFAULT_Q) for action in ActionType.ALL_ACTIONS])

                # calculate q for current state
                q = self.Q.get((currentState, randomAction), config.DEFAULT_Q)
                self.Q[(currentState, randomAction)] = q + config.Q_ALPHA * (reward + config.Q_GAMMA * maxQ - q)

                self.log_saving_new_q_value(currentState, randomAction, reward, self.Q[(currentState, randomAction)],
                                            nextState)

                # update the world with next state
                self.wm.update(randomAction)

                if self.is_episode_finished():
                    break

            self.log_ending_episode(i + 1)
            self.save_learned_data()

    def calculate_reward(self):
        state = self.wm.get_current_state()
        positiveAngle = self.get_positive_angle(state.angle)
        minDistanceFromWall = min(state.pos, config.SPACE_WIDTH - state.pos)

        reward = (180 - positiveAngle) + 1.0 / 4.0 * minDistanceFromWall
        return reward

    def is_episode_finished(self):
        state = self.wm.get_current_state()
        positiveAngle = self.get_positive_angle(state.angle)
        if positiveAngle < 0.5 and abs(state.w) < 0.05 and abs(state.vel) < 0.15:
            self.num_of_success_repeat += 1
            if self.num_of_success_repeat >= config.SUCCESS_REPEATS:
                return True
        else:
            self.num_of_success_repeat = 0

        minDistanceFromWall = min(state.pos, config.SPACE_WIDTH - state.pos)
        if minDistanceFromWall < 0.01:
            self.num_of_is_near_wall += 1
            if self.num_of_is_near_wall >= config.NEAR_WALL_REPEATS:
                return True
        else:
            self.num_of_is_near_wall = 0

        return False

    def get_positive_angle(self, angle):
        positiveAngle = 0
        if angle < 0:
            if -180 <= angle:
                positiveAngle = abs(angle)
            else:
                positiveAngle = 360 - abs(angle)
        elif angle > 0:
            if angle <= 180:
                positiveAngle = angle
            else:
                positiveAngle = 360 - angle

        return positiveAngle

    def log_start_episode(self, episodeNum):
        print "\nStart Learning new episode(" + str(episodeNum) + "/" + str(self.episode_num) + ")"

    def log_saving_new_q_value(self, currentState, action, reward, q, newState):
        print "current state:", currentState
        print "did action:", action
        print "entered state:", newState
        print "rewarded:", reward
        print "updating Q for [ (" + str(currentState.angle) + "," + str(currentState.pos) + "), " + str(
                action) + " ] =", q
        print "exploration percent:", str(len(self.Q) / (120 * 10.0 * 3) * 100), "( " + str(len(self.Q)) + "/" + str(
            120 * 10 * 3) + ")"
        print '\n'

    def log_ending_episode(self, episodeNum):
        print "Ending episode: " + str(episodeNum)
        print "--------------------------------------------"

    def save_learned_data(self):
        with open(config.LEARNED_DATA["path"], 'wb') as f:
            pickle.dump(self.Q, f, pickle.HIGHEST_PROTOCOL)

    def load_learned_data(self):
        if not os.path.exists(config.LEARNED_DATA["path"]):
            if not os.path.exists(config.LEARNED_DATA["dir"]):
                os.mkdir(config.LEARNED_DATA["dir"])

            open(config.LEARNED_DATA["path"], 'a').close()
        else:
            if os.stat(config.LEARNED_DATA["path"]).st_size != 0:
                with open(config.LEARNED_DATA["path"], 'rb') as f:
                    self.Q = pickle.load(f)
