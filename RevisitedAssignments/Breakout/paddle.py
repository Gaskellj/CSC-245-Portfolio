import pygame

class Paddle:

    def __init__(self, x_pos, y_pos, x, y):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, "White", pygame.Rect(self.x_pos, self.y_pos, self.x, self.y))
