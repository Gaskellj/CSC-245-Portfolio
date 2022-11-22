##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## Updates: John Rieffel, Fall 2022
## James Gaskell, Fall 2022
##
## This file defines a ball class that can move in two dimensions and
## can bounce off other balls.
##

from hashlib import new
import imp
import pygame
import math

from vector import Vector
from ball_2d import Ball

class MovingBall (Ball):

    v = Vector(0.0, 0.0)

    friction_coefficient = 0.9999

    speedlimit = 500

    e = 0.2

    moving = False

    def __init__ (self, x, y, r, m, color, xv, yv, ball_name, ball_value, original_position):

        Ball.__init__(self, x, y, r, m, color)

        self.v = Vector(float(xv),float(yv))

        self.ball_name = ball_name

        self.value = ball_value

        self.spot_position = original_position


    def simulate (self, dt, width, height):
        self.move (dt)
        self.friction()
        self.bounce_rail (width, height)


    def move (self, dt):

        self.p = self.p + self.v


    def clamp_v (self):
        '''
        clamp max speed
        '''
        if self.v.length() > self.speedlimit:
            self.v.normalize()
            self.v = self.v * float(self.speedlimit)
            

    def bounce_rail (self, table_width, table_height):
        '''
        handle bounces and readjust to prevent penetration
        '''
        if self.p.x < 78+self.r:
            self.p.x = 78+self.r
            self.v.x *= -1
            self.v *= 0.9
        elif self.p.x > 83+table_width-self.r:
            self.p.x = 83+table_width-self.r
            self.v.x *= -1
            self.v *= 0.9
        if self.p.y < 78+self.r:
            self.p.y = 78+self.r
            self.v.y *= -1
            self.v *= 0.9
        elif self.p.y > 85+table_height-self.r:
            self.p.y = 85+table_height-self.r
            self.v.y *= -1
            self.v *= 0.9

    def collide_object (self, other):
        """ Check whether there is a collision with another object. If
        so, calculate the impulse j due to the impact and apply
        impulse to both objects."""
        o = other
        n = self.collide(o)  
        if n != None:
            j = (-(1+self.e)*(self.v-(o.v)).dot(n))/(n.dot(n)*(1/self.m + 1/o.m))
            self.apply_impulse (j, n)
            o.apply_impulse (-j, n)
            return n


    def collide (self, other):
        """
        Checks whether two circles collide. If they do and are already
        intersecting, they get moved apart a bit. The return value is
        None if there is no collision, and the vector pointing from
        the center of the first to the center of the second ball if
        there is a collision.
        """

        d = self.p - other.p
        if d.length() < self.r + other.r:
            self.repair_position (d, other)
            return d
        else:
            return None


    def apply_impulse (self, j, n):
        """ j is the impulse; n the collision normal, i.e. the
        direction along which the impact happens."""
        
        self.v = self.v + n * (j / self.m)

    def repair_position (self, rel_pos, other):
        """ If two objects overlap, move them apart so that they are
        touching but not overlapping. How much each of the objects
        gets moved depends on its mass, so that objects with an
        infinite mass do not get moved."""

        # dividing by 10, because the length of our normal vector is 10 pixels
        repair = float(self.r + other.r - rel_pos.length())#/10
        rel_pos.normalize()
        if math.isinf (self.m):
            other.p = other.p + (rel_pos *-1*repair)
        elif math.isinf (other.m):
            self.p = self.p + (rel_pos* repair)
        else:
            self.p = self.p + (rel_pos*repair*(other.m/(self.m+other.m)))
            other.p = other.p + (rel_pos* -1 * repair*(self.m/(self.m+other.m)))

    def getResponse(self,other,normvector):
        return Vector(0,0)

    def bounce (self, j, n):

        self.v = self.v +_ (n * (j / self.m))
        self.clamp_v ()

    def setVelocity(self,v):
        self.v = v

    def friction(self):

        ## Slows balls down as they move along the table due to friction
        # Uses a friction coefficicient that increases over time to make it seem realistic

        self.v *= self.friction_coefficient
        self.friction_coefficient = self.friction_coefficient  **1.003
        if abs(self.v.x) < 0.01:
            self.setVelocity(Vector(0,self.v.y))
            if abs(self.v.y) <= 0.1:
                self.setVelocity(Vector(self.v.x,0))
        if abs(self.v.y) < 0.01:
            self.setVelocity(Vector(self.v.x,0))
            if abs(self.v.x) <= 0.1:
                self.setVelocity(Vector(0,self.v.y))
        if abs(self.v.x) == 0 and abs(self.v.y) == 0:
            self.friction_coefficient = 0.99999

    def collide_pockets_red (self, ball_list, pocket_list, potted_balls):

        ## Checks if reds are potted
        # Used for colors when they do not require a respot (acting like reds)

        for p in pocket_list:
            position = Vector(p.x,p.y)
            d = self.p - position
            if d.length() < self.r + p.r:
                ball_list.remove(self)
                potted_balls.append(self.value)

    def collide_pockets_color(self, ball_list, pocket_list, potted_balls, respot_list):

        ## Checks if colors are potted
        # Adds potted balls to the respot list to be re-added to the game
        # Initialises their positions to their original spots and their velocities to 0

        for p in pocket_list:
            position = Vector(p.x,p.y)
            d = self.p - position
            if d.length() < self.r + p.r:
                self.p.x = self.spot_position.x
                self.p.y = self.spot_position.y
                self.v = Vector(0,0)
                potted_balls.append(self.value)
                respot_list.append(self)
                ball_list.remove(self)

    def collide_pockets_cueball(self, pocket_list):

        ## Checks is the white is potted
        # Returns true if potted

        white_potted = False
        for p in pocket_list:
            position = Vector(p.x,p.y)
            d = Vector(self.p.x,self.p.y) - position
            if d.length() < self.r + p.r:
                white_potted = True
        return white_potted
