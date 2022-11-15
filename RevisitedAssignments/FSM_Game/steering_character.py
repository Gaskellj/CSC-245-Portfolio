import random
import math
import pygame
from moving_ball_2d import MovingBall
from vector import Vector


class BeakBall (MovingBall):

    beak_tip = Vector(0,20)
    max_acceleration = 200.0

    speedlimit = Vector(500,500)

    steering = []

    color_list = ['pink','blue','yellow','purple','orange']

    angle = 0
    radius = 2

    def draw (self, window):
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 5
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
        random_x = self.r * random.uniform(-1,1)
        random_y = self.r * random.uniform(-1,1)
        target = Vector(random_x,random_y)
        max_speed = self.speedlimit.length()
        desired_velocity = target * max_speed
        for i in range(0,10):
            self.steering += [(desired_velocity - self.v) * weight]
    
    def teleport(self):
        print('Sprite Teleported')
        self.v = Vector(0,0)
        self.p.x = random.randint(512,1024)
        self.p.y = random.randint(384,768)
    
    def change_color(self):
        self.color = random.choice(self.color_list)

    def loop(self,weight):
        self.color = 'orange'
        self.radius = self.radius + 0.01
        x = int(math.cos(self.angle) * 3) + self.p.x
        y = int(math.sin(self.angle) * 3) + self.p.y
        self.p.x = x
        self.p.y = y
        self.angle += 0.05
        random_x = self.r * random.uniform(-1,1)
        random_y = self.r * random.uniform(-1,1)
        target = Vector(random_x*10,random_y*10)
        max_speed = self.speedlimit.length()
        desired_velocity = target * max_speed
        for i in range(0,10):
            self.steering += [(desired_velocity - self.v) * weight]

    def freeze(self):
        self.v = Vector(0,0)





