import pygame
import random

class brick:

    def __init__ (self, x, y, color):
        self.y = y
        self.x = x
        self.rect = pygame.Rect((x,y,50,20))
        self.color = pygame.Color(color)
        self.powerup = random.randint(0,10)

    def draw(self, window):
        pygame.draw.rect(window,self.color,self.rect)


