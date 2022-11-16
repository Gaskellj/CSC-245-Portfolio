##
## Author: Kristina Striegnitz
## Author: John Rieffel 
##
## Version: Fall 2022 
##
## A character shows a simple seek behavior that makes it move towards
## a target.
##

import pygame
import random
import time
from time import sleep

from vector_2 import Vector
from steering_ball import SteeringBall
from moving_ball_2d import MovingBall
from world import World

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 1024
    height = 768
    my_win = pygame.display.set_mode((width,height))

    boids = []
    number_of_boids = 20

    ## setting up the game world
    world = World (width, height)

    ## our character
    for i in range (0,number_of_boids):
        x = random.randint(0,width)
        y = random.randint(0,height)
        c = SteeringBall (x, y, 10, 1, pygame.color.Color("darkorange"), 0, 0)
        boids.append(c)

    ## the target
    target = MovingBall (150, 175, 20, float('inf'), pygame.color.Color("red"), 0, 0)

    target2 = MovingBall (random.randint(0,width), random.randint(0,height), 10, float('inf'), pygame.color.Color("blue"), random.randint(-10,10), random.randint(-10,10))

    centroid = MovingBall (0, 0, 3, float('inf'), pygame.color.Color("green"), 0, 0)
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):

        dt = clock.tick(60)
        if dt > 500:
            continue

        ## Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                mousepos = pygame.mouse.get_pos()
##                mousepos = Vector(mousepos[0],mousepos[1])
##                target.p = mousepos
                


        mousepos = pygame.mouse.get_pos()
        mousepos = Vector(mousepos[0],mousepos[1])
        target.p = mousepos
        
        ## Simulate game world
        target.move (dt, world)
        target2.simulate(dt, world)
        target.collide_edge (world)

        cumulative_x = 0
        cumulative_y = 0
        
        my_win.fill(pygame.color.Color("gray14"))

        for index in boids:
            index.steering = []
            index.wander(1.0/30)
            index.fleeing(target,1.0/30)
            index.arriving(target2, 1.0/30)
            index.cohesion(centroid, 0.01)
            index.separation(boids, 2)
            #index.align(boids, number_of_boids)
            index.apply_steering()
            index.move(dt, world)
            index.collide_edge (world)

            cumulative_x += index.p.x
            cumulative_y += index.p.y
        
            ## Rendering
            # Draw frame
            index.draw(my_win)
        

        centroid.p.x = cumulative_x / number_of_boids
        centroid.p.y = cumulative_y / number_of_boids
        centroid.draw(my_win)
        
        target.draw(my_win)
        target2.draw(my_win)

        # Swap display
        pygame.display.update()

        ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
