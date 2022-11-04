from calendar import c
from hashlib import new
from lib2to3.pytree import convert

import pygame
import random

from brick_2d import brick
from Paddle import paddle
from moving_ball_sprite_2d import MovingBall

from time import sleep
from tkinter import *

def game_won():

        pygame.init()
        width = 400
        height = 200
        window = pygame.display.set_mode((width,height))
        window.fill(pygame.color.Color("black"))

        font = pygame.font.Font('freesansbold.ttf', 25)

        keepGoing = True    
        while (keepGoing):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

            text = font.render("Congratulations, you have won", True, 'green')
            textRect = text.get_rect()
            textRect.center = (200, 100)
            window.blit(text, textRect)

            pygame.display.update()

def run_game():

    pygame.init()

    blocks = []
    balls = []
    block_colors = [[253,127,25],[251,181,51],[252,238,175],[234,32,20],[79,111,35]]

    gamewon = False

    score = 0
    font = pygame.font.Font('freesansbold.ttf', 16)

    game_paddle = paddle()
    
    width = 600
    height = 480
    window = pygame.display.set_mode((width,height))
    window.fill(pygame.color.Color("black"))

    x = 0
    y = 30
    for i in range(0,5):
        for z in range(0,12):
            block1 = brick(x,y,block_colors[i])
            x = x + 50
            blocks.append(block1)
        y = y + 20
        x = 0
    
    dt = 0
    ball = MovingBall (200, height/2, 7, 10, pygame.color.Color("white"), .2, .2)
    balls.append(ball)

    keepGoing = True    
    while (keepGoing):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        window.fill(pygame.color.Color("black"))

        for b in blocks:
            b.draw(window)

        for b in balls:
            b.simulate(dt, width, height)
        
        for b in balls:
            b.draw(window)

        mouse_x, y = pygame. mouse. get_pos()

        if mouse_x <= 37.5:
            game_paddle.change_position(37.5)
        elif mouse_x >= 562.5:
            game_paddle.change_position(562.5)
        else:
            game_paddle.change_position(mouse_x)
        

        game_paddle.draw(window,"white")

        Score = ("Score = ", str(score))

        text = font.render("Score = " + str(score), True, 'green')
        textRect = text.get_rect()
        textRect.center = (60, 430)
        window.blit(text, textRect)

        pygame.display.update()


        for event in pygame.event.get():
            try:
                x = random.randint(0,len(blocks)-1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        blocks.pop(x)
                        score = score + 100
                        if len(blocks) == 0:
                            gamewon = True
            except ValueError:
                pygame.QUIT
                game_won()
                keepGoing = False


run_game()