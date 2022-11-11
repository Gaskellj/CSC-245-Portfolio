##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## Updates: John Rieffel, Fall 2022
##
## This file defines a ball class that can move in two dimensions and
## can bounce off other balls.

from hashlib import new
import pygame
import math

from vector import Vector
from ball_2d import Ball

class MovingBall (Ball):

    v = Vector(0.0, 0.0)

    speedlimit = 500

    def __init__ (self, x, y, r, m, color, xv, yv):

        Ball.__init__(self, x, y, r, m, color)

        self.v = Vector(float(xv),float(yv))


    def simulate (self, dt, width, height):
        self.move (dt)
        self.bounce_wall (width, height)


    def move (self,dt):

        self.p = self.p + self.v


    #def clamp_v (self):
        '''
        clamp max speed
        '''
        #if self.v.length() > self.speedlimit:
            #self.v.normalize()
            #self.v = self.v * float(self.speedlimit)
            

    def bounce_wall (self, width, height):
        '''
        handle bounces and readjust to prevent penetration
        '''
        if self.p.x < 0+self.r:
            self.p.x = self.r
            self.v.x *= -1
        elif self.p.x > width-self.r:
            self.p.x = width-self.r
            self.v.x *= -1
        if self.p.y < 0+self.r:
            self.p.y = self.r
            self.v.y *= -1
        elif self.p.y > height-self.r:
            self.p.y = height-self.r
            self.v.y *= -1
            


    #def collide (self, other):
        """
        Checks whether two circles collide. If they do and are already
        intersecting, they get moved apart a bit. The return value is
        None, if there is no collision, and the vector pointing from
        the center of the first to the center of the second ball if
        there is a collision.
        """
        #d = self.p - other.p
        #print d
        #if d.length() < self.r + other.r:
            #print("collide:", self.p, other.p, self.p.minus(other.p))
            #repair = float(self.r + other.r - d.length())
            #d.normalize()
            #print self.p, other.p
            #self.p = self.p + (repair*d)
            #other.p = other.p + (-1*repair*d)
            #print repair, self.p, other.p
            #return d
        #else:
            #return None

    #def getResponse(self,other,normvector):
                    # new velocity is 
                    # v1_normal' = v1_normal*(m1-m2)+2*m2*v2_normal
                    #              ----------------------------      
                    #                   m1 + m2
        #return Vector(0,0)

    #def bounce (self, j, n):

        #self.v = self.v + (n * (j / self.m))
        #self.clamp_v ()

    #def setVelocity(self,v):
        #self.v = v
