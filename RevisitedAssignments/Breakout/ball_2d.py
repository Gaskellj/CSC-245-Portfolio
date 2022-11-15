##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## This file defines a simple ball class. The ball is stationary; we
## just get to define its position, size and color. This
## implementation uses the vector class.

import pygame

from vector import Vector

class Ball:

    p = Vector(0.0,0.0)

    m = 0.0

    color = pygame.color.Color('darkgreen')


    def __init__ (self, x, y, width, height, m, color):
        self.p = Vector(float(x), float(y))
        self.w = width
        self.h = height
        self.m = float(m)
        self.color = color

        
    def draw (self, window):
        pygame.draw.rect(window,self.color, pygame.Rect(self.p.x, self.p.y, self.w, self.h))

