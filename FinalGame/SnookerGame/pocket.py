##
## Author: James Gaskell
##
## Version: Fall 2022
##

import pygame

class Pocket:

    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.r = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (23, 32, 42),(self.x,self.y), self.r)
    