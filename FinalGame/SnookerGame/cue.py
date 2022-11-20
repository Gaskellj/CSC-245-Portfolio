##
## Author: James Gaskell
##
## Version: Fall 2022
##


import pygame
from math import *

class CueStick:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.c = color
        self.length = length
        self.tangent = 0

    def hit_ball(self, cue_ball, force):
        print(self.tangent)
        print(force)

    def draw(self, surface, cuex, cuey):
        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = (degrees(atan2((cuey - self.y), (cuex - self.x))))
        pygame.draw.line(surface, (0,0,0), (cuex + self.length*cos(radians(self.tangent)), cuey + self.length*sin(radians(self.tangent))), (cuex, cuey), 1)
        pygame.draw.line(surface, self.c, (self.x, self.y), (cuex, cuey), 3)