import pygame
from math import *

class launcher:
    def __init__(self, x, y, length, color):
        self.x = x
        self. y = y
        self.c = color
        self.length = length
        self.tangent = 0

    def draw(self, surface, ballx, bally):

        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = (degrees(atan2((bally - self.y), (ballx - self.x))))
        pygame.draw.line(surface, (0,0,0), (ballx + self.length*cos(radians(self.tangent)), bally + self.length*sin(radians(self.tangent))), (ballx, bally), 1)
        pygame.draw.line(surface, self.c, (self.x, self.y), (ballx, bally), 3)