

from steering_character import BeakBall
from fsm import FSM
from world import World

class FSMBeakBall (BeakBall):

    def __init__ (self, x, y, r, m, color, xv, yv, world):

        BeakBall.__init__(self, x, y, r, m, color, xv, yv)

        self.fsm = FSM()

        # green - wander; red - run
        self.fsm.add_states ([('wandering', lambda:self.wander(1.0/30)),('looping', lambda:self.loop(1.0/30)),('teleport', lambda:self.teleport()), ('color_changing', lambda:self.change_color()), ('freezing', lambda:self.freeze())])
        
        self.fsm.add_transitions ('wandering', [(self.test_on_red, 'looping'), (self.test_on_black_GreenSide, 'teleport'), (self.test_on_outskirts, 'freezing')])
        self.fsm.add_transitions ('looping', [(self.test_on_green, 'wandering'), (self.test_on_black_RedSide, 'color_changing'), (self.test_on_outskirts, 'freezing')])
        self.fsm.add_transitions ('teleport', [(self.test_on_red, 'looping')])
        self.fsm.add_transitions ('color_changing', [(self.test_on_red, 'looping')])


    def execute_actions (self):

        self.steering = []

        action = self.fsm.states[self.fsm.current_state]
        action()

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

    def test_on_black_GreenSide (self,world):
        if ((self.p.x > world.width/4 - 50 and self.p.x < world.width/4 + 50) and (self.p.y > world.height/2 -50 and self.p.y < world.height/2 + 50)):
            return True
        else:
            return False

    def test_on_black_RedSide (self,world):
        if ((self.p.x > (world.width - world.width/4 - 50) and self.p.x < (world.width - world.width/4 + 50) and (self.p.y > world.height/2 -50 and self.p.y < world.height/2 + 50))):
            return True
        else:
            return False

    def test_on_outskirts (self,world):
        if (self.p.x < self.r * 2) or (self.p.y < self.r * 2) or (self.p.x > (world.width - self.r * 2)) or (self.p.y > (world.height - self.r * 2)):
            return True
        else:
            return False



