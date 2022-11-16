

from steering_character import BeakBall
from fsm import FSM
from world import World
from vector import Vector
from moving_ball_2d import  MovingBall

class FSMBeakBall (BeakBall):

    def __init__ (self, x, y, r, m, color, xv, yv, world):

        BeakBall.__init__(self, x, y, r, m, color, xv, yv)

        self.fsm = FSM()

        target = MovingBall

        # green - wander; red - run
        self.fsm.add_states ([('wandering', lambda:self.arriving(target,1.0/30)),('fleeing', lambda:self.fleeing(target,1.0/30))])
        
        self.fsm.add_transitions ('wandering', [(self.test_on_red, 'fleeing')])
        self.fsm.add_transitions ('fleeing', [(self.test_on_green, 'wandering')])


    def execute_actions (self, target, boids):

        self.steering = []

        if self.fsm.current_state == "wandering":
            self.arriving(target,1.0/30)
            self.separation(boids, 3)
        elif self.fsm.current_state == "fleeing":
            self.fleeing(target,1.0/30)

        self.apply_steering ()


    def test_on_red (self, world):

        if self.p.x > world.width/2 :
            return True
        else:
            return False

    def test_on_green (self, world):
        if self.p.x <= world.width/2 :
            return True
        else:
            return False






