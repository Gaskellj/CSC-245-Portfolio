##
## Author: James Gaskell
##
## Version: Fall 2022 
##

import math
import pygame
import random
from cue import CueStick

from moving_ball_sprite_2d import MovingBall
from vector import Vector
from rail import Rail
from pocket import Pocket

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    myFont = pygame.font.Font(None,30)

    balls= []
    rail_list = []
    pocket_list = []
    moves_history = []
    current_break = []
    potted_balls = []
    respot_list = []
    
    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))

    ## important properties of the environment

    ## initialize the balls

    # elasticity coefficient
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0

    white = (236, 240, 241)

    table_color = (93, 41, 6)
    cloth_color = (10, 108, 3)

    black = (23, 32, 42)
    yellow = (244, 208, 63)
    blue = (0, 0, 139)
    red = (139, 0, 0)
    green = (1,50,32)
    brown = (101, 67, 33)
    pink = (199,21,133)
    stickColor = (249, 231, 159)

    table_width = width - 163
    table_height = height - 263

    create_table(pocket_list, rail_list, table_width, table_height)


    ball_mass = 1.0
    ball_radius = 7

    create_balls(table_height, table_width, balls, red, yellow, green, brown, blue, black, pink, ball_mass, ball_radius)

    cue_ball = MovingBall(84+4/5*table_width, table_height/2+65, 7, ball_mass,  white, 0,0, "cue", -4, Vector (84+4/5*table_width, table_height/2+65))

    cue = CueStick(0,0,50,stickColor)


    ## The game loop starts here.

    ball_moving = False

    player1_Score = ["", 0]
    player2_Score = ["", 0]

    current_player = player1_Score


    introP1 = True
    introP2 = True
    keepGoing = True

    #########
    ## The intro screen: lets the player input a name
    #########
    while introP1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introP1 = False
                keepGoing = False

            elif event.type==pygame.KEYDOWN:

                if event.key >= 65 and event.key <= 122:
                    player1_Score[0] += chr(event.key)

                if event.key == pygame.K_BACKSPACE:
                    player1_Score[0] = (player1_Score[0])[:-1]

                if event.key == 13:
                    introP1 = False

        ## Draw picture and update display
        my_win.fill(pygame.color.Color(cloth_color))

        label = myFont.render("Please enter Player1's name: "+player1_Score[0], True, pygame.color.Color(black))
        my_win.blit(label, (50,height/2-100))

        label = myFont.render("Then hit 'Enter.'", True, pygame.color.Color(black))
        my_win.blit(label, (50,height/2-50))

        pygame.display.update()

    while introP2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introP2 = False
                keepGoing = False

            elif event.type==pygame.KEYDOWN:

                if event.key >= 65 and event.key <= 122:
                    player2_Score[0] += chr(event.key)

                if event.key == pygame.K_BACKSPACE:
                    player2_Score[0] = (player2_Score[0])[:-1]

                if event.key == 13:
                    introP2 = False

        ## Draw picture and update display
        my_win.fill(pygame.color.Color(cloth_color))

        label = myFont.render("Please enter Player 2's name: "+player2_Score[0], True, pygame.color.Color(black))
        my_win.blit(label, (50,height/2-100))

        label = myFont.render("Then hit 'Enter' to start.", True, pygame.color.Color(black))
        my_win.blit(label, (50,height/2-50))

        pygame.display.update()

    my_win = pygame.display.set_mode((width+100,height+100))

    while (keepGoing):

        potted_balls = []


        #dt = clock.tick(50)
        #print dt

        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            if event.type == pygame.MOUSEBUTTONDOWN and ball_moving == False:
                start = Vector(cue_ball.p.x, cue_ball.p.y)
                x, y = pygame.mouse.get_pos()
                end = Vector(x ,y)
                start -= end
                dist = start.length()
                start.normalize()
                force = dist/200.0
                if force > 1:
                    force = 1
                
                start *= force
                cue_ball.v = start

            print(player1_Score)
            print(player2_Score)

                

        ## Simulate game world
        for b in balls:
            b.simulate(dt, width, height)

        #print b1.v

        ## Draw frame
        
        my_win.fill(pygame.color.Color("gray14"))


        for b in balls:
                b.draw(my_win)
                b.bounce_rail(table_width, table_height)

        pygame.draw.rect(my_win, cloth_color, pygame.Rect(75, 75, width-150, height-250))

        draw_baulk_line(my_win, table_width,table_height, black, cloth_color)

        for rail in rail_list:
            rail.draw(my_win)

        pygame.draw.rect(my_win, table_color, pygame.Rect(50, 50, width-100, height-200),  16, 20)



        for pocket in pocket_list:
            pocket.draw(my_win)

        cue_ball.simulate(dt, table_width, table_height)

        cue_ball.draw(my_win)

        for ball in balls:
            ball.draw(my_win)


        for i in range(0,len(balls)):
            b1 = balls[i]
            for j in range(i+1,len(balls)):
                b2 = balls[j]
               #calculate normal of collission
                b1.collide_object(b2)
                #if n != None:
                    #print("do something here")

        ball_moving = False
        for b in balls:
            n = b.collide_object(cue_ball)
            if n != None:
                cue_ball.v *= 0.95
                b.v *= 0.95
            if b.value == 1:
                b.collide_pockets_red(balls,pocket_list, potted_balls)
            elif b.value > 1:
                b.collide_pockets_color(balls, pocket_list, potted_balls, respot_list)
            if b.v.x !=0 or b.v.y != 0:
                ball_moving = True
        if cue_ball.v.x != 0 or cue_ball.v.y != 0:
            ball_moving = True

        if not ball_moving:
            cue.draw(my_win,cue_ball.p.x, cue_ball.p.y)
            for r in respot_list:
                balls.append(r)
            respot_list.clear()


        Foul = False

        if(len(potted_balls)) > 0:
            for i in range(0,len(potted_balls)-1):
                if potted_balls[i] == potted_balls[i+1]:
                    pass
                else:
                    Foul = True
            if not Foul:
                for value in potted_balls:
                    current_break.append(value)

        label = myFont.render(player1_Score[0] + "'s Score = " + str(player1_Score[1]), True, pygame.color.Color(cloth_color))
        my_win.blit(label, (50,height-100))

        label = myFont.render(player2_Score[0] + "'s Score = " + str(player2_Score[1]), True, pygame.color.Color(cloth_color))
        my_win.blit(label, (50,height-50))
        
        ## Swap display

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


def create_table(pList, rList, table_width,table_height):
    pockett_top_left = Pocket(78,78,16)
    pocket_bottom_left = Pocket(78,86+table_height,16)
    pocket_top_middle = Pocket(78+(table_width/2),72,16)
    pocket_bottom_middle = Pocket(78+(table_width/2),91+table_height,16)
    pocket_top_right = Pocket(86+table_width,78,16)
    pocket_bottom_right = Pocket(86+table_width,86+table_height,16)
    pList.append(pockett_top_left)
    pList.append(pocket_bottom_left)
    pList.append(pocket_top_middle)
    pList.append(pocket_bottom_middle)
    pList.append(pocket_top_right)
    pList.append(pocket_bottom_right)

    side_left_rail = Rail(65,75,13,table_height)
    right_side_rail = Rail(84+table_width,75,13,table_height)
    bottom_rail = Rail(65,table_height+86,table_width+28,13)
    top_rail = Rail(65,65,table_width+28,13)

    rList.append(side_left_rail)
    rList.append(right_side_rail)
    rList.append(bottom_rail)
    rList.append(top_rail)

def draw_baulk_line(surface, table_width,table_height, black, green):
    pygame.draw.line(surface, black,((75+4/5*table_width),75),(75+4/5*table_width,table_height+100),1)
    pygame.draw.circle(surface, black, (75+4/5*table_width, table_height-25), 40,1)
    pygame.draw.rect(surface, green, pygame.Rect(35+4/5*table_width, table_height-65, 40,80))

def create_balls(table_height, table_width, balls, red, yellow, green, brown, blue, black, pink, ball_mass, ball_radius):
    black_ball = MovingBall(75+1/11*table_width, table_height-25,ball_radius,ball_mass,black,0,0,"black",7, Vector(75+1/11*table_width, table_height-25))
    pink_ball = MovingBall(75+3/11*table_width, table_height-25,ball_radius,ball_mass,pink,0,0,"pink",6, Vector(75+3/11*table_width, table_height-25))
    blue_ball = MovingBall(75+1/2*table_width, table_height-25,ball_radius,ball_mass,blue,0,0,"blue",5, Vector(75+1/2*table_width, table_height-25))
    brown_ball = MovingBall(75+4/5*table_width, table_height-25,ball_radius,ball_mass,brown,0,0,"brown",4, Vector(75+4/5*table_width, table_height-25))
    green_ball = MovingBall(75+4/5*table_width, table_height-65,ball_radius,ball_mass,green,0,0,"green",3, Vector(75+4/5*table_width, table_height-65))
    yellow_ball = MovingBall(75+4/5*table_width, table_height+15,ball_radius,ball_mass,yellow,0,0,"yellow",2, Vector(75+4/5*table_width, table_height+15))
    red1 = MovingBall(pink_ball.p.x - 20, table_height-25,ball_radius,ball_mass,red,0,0,"red",1,Vector(pink_ball.p.x - 20, table_height-25))
    red2 = MovingBall(red1.p.x - 11, red1.p.y+ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red1.p.x - 11, red1.p.y+ball_radius))
    red3 = MovingBall(red1.p.x - 11, red1.p.y-ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red1.p.x - 11, red1.p.y-ball_radius))
    red4 = MovingBall(red2.p.x - 11, red2.p.y+ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red2.p.x - 11, red2.p.y+ball_radius))
    red5 = MovingBall(red2.p.x - 11, red2.p.y-ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red2.p.x - 11, red2.p.y-ball_radius))
    red6 = MovingBall(red3.p.x - 11, red3.p.y-ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red3.p.x - 11, red3.p.y-ball_radius))
    red7 = MovingBall(red4.p.x - 11, red4.p.y+ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red4.p.x - 11, red4.p.y+ball_radius))
    red8 = MovingBall(red4.p.x - 11, red4.p.y-ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red4.p.x - 11, red4.p.y-ball_radius))
    red9 = MovingBall(red6.p.x - 11, red6.p.y+ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red6.p.x - 11, red6.p.y+ball_radius))
    red10 = MovingBall(red6.p.x - 11, red6.p.y-ball_radius, ball_radius,ball_mass,red,0,0,"red",1, Vector(red6.p.x - 11, red6.p.y-ball_radius))


    balls.append(black_ball)
    balls.append(pink_ball)
    balls.append(blue_ball)
    balls.append(brown_ball)
    balls.append(green_ball)
    balls.append(yellow_ball)
    balls.append(red1)
    balls.append(red2)
    balls.append(red3)
    balls.append(red4)
    balls.append(red5)
    balls.append(red6)
    balls.append(red7)
    balls.append(red8)
    balls.append(red9)
    balls.append(red10)
    pass


## Start game
run_game()

