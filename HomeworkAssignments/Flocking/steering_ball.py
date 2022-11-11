
import pygame
from moving_ball_2d import MovingBall
from vector_2 import Vector


class SteeringBall (MovingBall):

    beak_tip = Vector(0,10)

    speedlimit = Vector(5000,5000)

    deceleration = 0

    # All steering inputs
    steering = []

    def draw (self, window):
        # draw the body
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        # draw the beak
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        #pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        if self.drawvec:
            for vec in self.steering:
                arrowvec = Vector(0,0)
                arrowvec = arrowvec + vec
                arrowvec = arrowvec + self.p
                 #pygame.draw.line(window,pygame.color.Color("red"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        ## add all steering inputs to current velocity vector
        for s in self.steering:
            self.v += s

    def arriving(self, target, weight):
        distance = (abs(self.p.x - target.p.x) + abs(self.p.y - target.p.y))**0.5
        required_distance = (self.r + target.r * 4)/5
        if distance > required_distance:
            self.seek(target, 1.0/30)
        else:
            speed_reduction = distance/required_distance
            desired_direction = (target.p - self.p).normalize()
            max_speed = self.speedlimit.length()
            desired_velocity = desired_direction * speed_reduction * max_speed
            self.steering += [(desired_velocity - self.v)*weight]

    def fleeing(self, target, weight):
        distance = (abs(self.p.x - target.p.x) + abs(self.p.y - target.p.y))**0.5
        required_distance = (self.r + target.r * 4)/5
        if distance < required_distance:
            desired_direction = (target.p - self.p).normalize()
            desired_direction.x = 0 - desired_direction.x
            desired_direction.y = 0 - desired_direction.y
            max_speed = self.speedlimit.length()
            desired_velocity = desired_direction * max_speed
            self.steering += [(desired_velocity - self.v)*weight]

    def seek(self, target, weight):

        #find difference between my location and target location 
        desired_direction = (target.p - self.p).normalize()
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        ## first find the "error" between current velocity and desired velocity, and then multiply that error 
        ## by the weight, and then add it to steering inputs
        self.steering += [(desired_velocity - self.v)*weight]

    def cohesion(self, centroid, weighting):
        desired_direction = (centroid.p - self.p).normalize()
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        self.steering += [(desired_velocity - self.v)* weighting]

    def separation(self, boids, weight):
        for i in boids:
            adjustment = Vector(0,0)
            distance_away = (abs(self.p.x - i.p.x) + abs(self.p.y - i.p.y))**0.5
            if distance_away <= 9:
                adjustment.x = adjustment.x - (self.p.x - i.p.x)
                adjustment.y = adjustment.y - (self.p.y - i.p.y)
            self.v -= adjustment*weight

    def align(self, boids, number_of_boids):
        TotalVelocity = Vector(0,0)
        for i in boids:
            TotalVelocity += i.v
        AverageVelocity = Vector((TotalVelocity.x - self.v.x)/(number_of_boids-1), (TotalVelocity.y - self.v.y)/(number_of_boids-1))
        Difference = AverageVelocity - self.v
        self.v = self.v + Difference/2

