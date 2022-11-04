import pygame

class brick:

    def __init__ (self, x, y, color):
        self.color = pygame.color.Color(color)
        self.rect = pygame.Rect(x,y,50,20)

    def draw(self, window):
        pygame.draw.rect(window,self.color,self.rect)


