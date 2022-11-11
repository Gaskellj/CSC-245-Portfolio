import pygame

class paddle:

    def __init__(self):
        self.mouse_position = 0

    def draw(self, window, color):
        pygame.draw.rect(window,color,pygame.Rect(self.mouse_position,400,75,15))


    def change_position(self, x_pos):
        self.mouse_position = x_pos - 37.5