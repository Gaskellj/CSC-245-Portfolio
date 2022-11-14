import random
import pygame
from moving_ball_2d import MovingBall
from vector import Vector


class BeakBall (MovingBall):

    beak_tip = Vector(0,20)
    max_acceleration = 200.0

    speedlimit = Vector(500,500)

    steering = []

    def draw (self, window):
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        for vec in self.steering:
            arrowvec = Vector(0,0)
            arrowvec = arrowvec + vec
            arrowvec = arrowvec + self.p
            pygame.draw.line(window,pygame.color.Color("red"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        for s in self.steering:
            self.v = self.v + s


    def wander(self,weight):
        random_x = self.r * 10 * random.randint(-1,1)
        random_y = self.r * 10 * random.randint(-1,1)
        target = Vector(random_x,random_y)
        desired_direction = (target.p - self.p).normalize()
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        self.steering += ((desired_velocity - self.v) * weight)
        print("wander:implement me")
        pass
    

    def loop(self,weight):
        '''
        agent should move in a corkscrew manner
        '''
        print("loop: implement me")
        pass

    def freeze(self,weight):
        self.v = Vector(0,0)
        print("freeze: implement me")
        pass


