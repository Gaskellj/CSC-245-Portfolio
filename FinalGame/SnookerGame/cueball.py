from time import sleep
from moving_ball_sprite_2d import MovingBall
from vector import Vector

class Cueball (MovingBall):
    
    def __init__ (self, x, y, r, m, color, xv, yv, ball_name, ball_value, original_position, FoulStatus):

        MovingBall.__init__(self, x, y, r, m, color, xv, yv, ball_name,ball_value, original_position)

        self.foul_status = FoulStatus    

    def place_ball(self, surface, balls, table_width, table_height, x, y):
        for b in balls:
            d = self.p - Vector(x,y)
            if d.length() < self.r + b.r:
                placed = False
            
            if placed:
                if x > 78+self.r and x < 83+table_width-self.r and y > 78+self.r and y < 85+table_height-self.r:
                    placed = True
        
        if placed:
            self.draw(surface)
            