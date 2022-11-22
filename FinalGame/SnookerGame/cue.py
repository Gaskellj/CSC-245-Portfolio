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

    def draw(self, surface, cuex, cuey):

        ## Draws the cue
        # Uses triganometry to solve for the direction the guide should be drawn on
        # Draws the guide - length can be adjusted by adjusting the length parameter in the main gama

        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = (degrees(atan2((cuey - self.y), (cuex - self.x))))
        pygame.draw.line(surface, (0,0,0), (cuex + self.length*cos(radians(self.tangent)), cuey + self.length*sin(radians(self.tangent))), (cuex, cuey), 1)
        pygame.draw.line(surface, self.c, (self.x, self.y), (cuex, cuey), 3)