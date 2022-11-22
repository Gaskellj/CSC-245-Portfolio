from moving_ball_sprite_2d import MovingBall

class Cueball (MovingBall):
    
    def __init__ (self, x, y, r, m, color, xv, yv, ball_name, ball_value, original_position, FoulStatus):

        MovingBall.__init__(self, x, y, r, m, color, xv, yv, ball_name,ball_value, original_position)

        self.foul_status = FoulStatus    
        

    def test_foul_occured(self):

        if self.foul_status == True:
            return True
        else:
            return False
    
    def test_no_foul(self):

        if self.foul_status == False:
            return True
        else:
            return False
            