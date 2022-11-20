##
## Author: James Gaskell
##
## Version: Fall 2022
##

import pygame

class Rail:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

        self.rect = pygame.Rect(x,y,width,height)


    def draw(self, surface):
        pygame.draw.rect(surface, (7,90,1), self.rect)

