##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## Illustrates collision balls.
## Starter code for Breakout
##

import pygame
import random

from moving_ball_sprite_2d import MovingBall
from vector import Vector
from paddle import Paddle
from bricks import brick

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    balls= []

    powerup_balls = []
    
    width = 600
    height = 480
    my_win = pygame.display.set_mode((width,height))

    ## important properties of the environment
    env = {'ground':height, 'g':100.0}

    ## initialize the balls

    b1 = MovingBall (random.randint(0,590), random.randint(300,400), 10,10,1.0,"White",1,-1)
    balls.append(b1)

    ## initialize the bricks

    bricks_list = []
    block_colors = [[253,127,25],[251,181,51],[252,238,175],[234,32,20],[79,111,35]]
    bezerk_colors = ['pink','blue','yellow','purple','orange']

    ## initialize the scoring and bezerk as false

    Score = 0
    bezerk = False
    bezerk_time = 0

    ## initialize font for score

    myFont = pygame.font.Font(None,30)


    x = 0
    y = 30
    for i in range(0,5):
        for z in range(0,12):
            b = brick(x,y,block_colors[i])
            x = x + 50
            bricks_list.append(b)
        y = y + 20
        x = 0

    paddle = Paddle(width/2-45,height-70,90,15)
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):


        dt = clock.tick(180)
        #print dt

        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                

        ## Simulate game world
        #for b in balls:
        [b.simulate(dt, width, height) for b in balls]

       
        #print b1.v

        ## Draw frame
        
        my_win.fill(pygame.color.Color("gray14"))

        collision = []

        for b in balls:
            b.check_collision_paddle(paddle)
            if b.p.y > height:
                balls.remove(b)
            if bezerk == True:
                b.check_bezerk_collision(bricks_list,collision)
            else:
                b.check_collision_brick(bricks_list,collision, powerup_balls)
            if len(collision) > 0:
                Score += 1
                print (Score)
            b.draw(my_win)

        x,y = pygame.mouse.get_pos()

        if x > 45 and x < width-45:
            paddle.x_pos = x-45


        #for item in bricks_list:
            #item.draw(my_win)
        [item.draw(my_win) for item in bricks_list] #Example of list comprehension

        [b.move(dt) for b in powerup_balls]  

        collision_paddle = False

        for b in powerup_balls:
            if b.check_collision_paddle_powerup(paddle) == True:
                print("powerup caught")
                powerup_balls.remove(b)
                bezerk_time += 720
            b.draw(my_win)

        paddle.draw(my_win)


        text = myFont.render("Score = " + str(Score), True, 'green')
        my_win.blit(text, (60,430))

        if bezerk_time > 0:
            if bezerk_time%10 == 0:
                for b in balls:
                    b.change_color(random.choice(bezerk_colors))
            bezerk = True
            bezerk_time -=1
        else:
            bezerk = False
            for b in balls:
                b.change_color("White")

        ## Swap display

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
