##
## Author: James Gaskell
##
## Version: Fall 2022 
##

import math
from re import T
import pygame
import random
from cue import CueStick

from moving_ball_sprite_2d import MovingBall
from vector import Vector
from rail import Rail
from pocket import Pocket
from cueball import Cueball

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    myFont = pygame.font.Font(None,30)

    balls= []
    rail_list = []
    pocket_list = []
    current_break = []
    potted_balls = []
    respot_list = []
    
    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))

    ## setting up the clock


    dt = 0

    ## Creates the color for the cueball

    white = (236, 240, 241)

    ## Creates the table color (brown) and the cloth color (green different to rails)

    table_color = (93, 41, 6)
    cloth_color = (10, 108, 3)

    ## Creates the colors for the balls

    black = (23, 32, 42)
    yellow = (244, 208, 63)
    blue = (0, 0, 139)
    red = (139, 0, 0)
    green = (1,50,32)
    brown = (101, 67, 33)
    pink = (199,21,133)

    ## Creates the cue color

    stickColor = (249, 231, 159)

    ## Marks the y and x values for the rightmost and bottommost part of the table 

    table_width = width - 163
    table_height = height - 263

    ## Runs the subroutine to initialise the table

    create_table(pocket_list, rail_list, table_width, table_height)


    ## Runs the subroutine to initialise the balls
    # All balls have mass of 1 and radius 7

    ball_mass = 1.0
    ball_radius = 7
    create_balls(table_height, table_width, balls, red, yellow, green, brown, blue, black, pink, ball_mass, ball_radius)

    ## Creates the cue and cueball

    cue_ball = Cueball(84+4/5*table_width, table_height/2+65, ball_radius, ball_mass,  white, 0,0, "cue", -4, Vector (84+4/5*table_width, table_height/2+65), False)
    cue = CueStick(0,0,100,stickColor)

    ## Initialises the variables that will track the state of the game
    
    ball_moving = False
    ball_in_hand = False

    shot_played = False
    ball_potted = False
    Foul = False

    ## Initialises the variables that will contain the player information (name and score)

    player1_Score = ["", 0]
    player2_Score = ["", 0]
    current_player = 1

    ## Ensures the player name selections and the main game play out in order
    # After the game is finished GameOver is used to inform the system to display the win/draw page

    introP1 = True
    introP2 = True
    keepGoing = True
    GameOver = False

    ## Initialises the list that will hold the high scores
    # Triggers subroutines that read in high scores from the file and order them

    HighScores = []
    find_high_scores(HighScores)
    sort_high_scores(HighScores)


    #########
    ## Intro screen: lets the player1 input a name
    #########
    while introP1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introP1 = False
                introP2 = False
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

    #########
    ## Intro screen: lets the player2 input a name
    #########

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

    #########
    ## The main gameloop
    #########

    while (keepGoing):

        ## clears thre pottedballs list every game loop

        potted_balls = []

        ## Quits the game if the window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            ## Checksif the player has ball in hand
            # If yes, the ball is placed where the user clicks
            # If no, the click is used with vector math to calculate the velocity and direction of the cueball

            if not ball_in_hand:
                if event.type == pygame.MOUSEBUTTONDOWN and ball_moving == False and ball_in_hand == False:
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

                    shot_played = True

            elif ball_in_hand:
                if event.type == pygame.MOUSEBUTTONDOWN and ball_moving == False and ball_in_hand == True:
                    x, y = pygame.mouse.get_pos()
                    print("ball placed")
                    cue_ball.p.x = x
                    cue_ball.p.y = y
                    cue_ball.place_ball(my_win, balls, table_width, table_height, x, y)
                    ball_in_hand = False



        ## Simulate game world
        for b in balls:
            b.simulate(dt, width, height)

        ## Draws frame
        # Outputs the scores, current break and Highest breaks list tothe screen
        
        my_win.fill(pygame.color.Color("gray14"))

        label = myFont.render(player1_Score[0] + "'s Score = " + str(player1_Score[1]), True, pygame.color.Color(cloth_color))
        my_win.blit(label, (50,height-110))

        label = myFont.render(player2_Score[0] + "'s Score = " + str(player2_Score[1]), True, pygame.color.Color(cloth_color))
        my_win.blit(label, (50,height-60))

        break_figure = sum(current_break)
        if break_figure < 0:
            break_figure = 0

        label = myFont.render("Current Break: " + str(break_figure), True, pygame.color.Color(cloth_color))
        my_win.blit(label, (width/2,height-110))

        label = myFont.render("Highest Breaks: ", True, pygame.color.Color(cloth_color))
        my_win.blit(label, (width/2,height-60))

        y = 20

        for score in HighScores:
            label = myFont.render(score[0]+ ": " + str(score[1]), True, pygame.color.Color(cloth_color))
            my_win.blit(label, (width/2,height-y))
            y -= 25


        if current_player == 1:
            name = player1_Score[0]
        else:
            name = player2_Score[0]

        label = myFont.render("Current Player: " + name, True, pygame.color.Color((7,90,1)))
        my_win.blit(label, (50,height))

        label = myFont.render("Current Player: " + name, True, pygame.color.Color((7,90,1)))
        my_win.blit(label, (50,height))

        for b in balls:
                b.draw(my_win)
                b.bounce_rail(table_width, table_height)

        ## Draws the rails, pockets and baulk line / Semicircle on the screen

        pygame.draw.rect(my_win, cloth_color, pygame.Rect(75, 75, width-150, height-250))
        draw_baulk_line(my_win, table_width,table_height, black, cloth_color)

        for rail in rail_list:
            rail.draw(my_win)

        pygame.draw.rect(my_win, table_color, pygame.Rect(50, 50, width-100, height-200),  16, 20)

        for pocket in pocket_list:
            pocket.draw(my_win)

        try:
            cue_ball.simulate(dt, table_width, table_height)
            cue_ball.draw(my_win)
        except NameError:
            pass

        ## Draws the balls on the table
        # Checks if a collision has taken place between the balls and rails


        for ball in balls:
            ball.draw(my_win)
            b.bounce_rail(table_width, table_height)


        ## Checks if collisions have taken place between balls

        for i in range(0,len(balls)):
            b1 = balls[i]
            for j in range(i+1,len(balls)):
                b2 = balls[j]
                b1.collide_object(b2)

        ## Checks if a collision has taken place between the cueball and balls
        # Checks if a collision has occured between balls and pockets
        # Checks if any balls are moving to decide wehter the turn is over and updates ball_moving variable


        ball_moving = False
        for b in balls:
            try:
                n = b.collide_object(cue_ball)
                if n != None:
                    cue_ball.v *= 0.95
                    b.v *= 0.95
            except NameError:
                pass
            if b.value == 1:
                b.collide_pockets_red(balls,pocket_list, potted_balls)
            elif b.value > 1 and len(balls) > 6:
                b.collide_pockets_color(balls, pocket_list, potted_balls, respot_list)
            elif b.value > 1 and len(balls) <= 6:
                b.collide_pockets_red(balls, pocket_list, potted_balls)

            if b.v.x !=0 or b.v.y != 0:
                ball_moving = True
        try:
            if cue_ball.v.x != 0 or cue_ball.v.y != 0:
                ball_moving = True
        except NameError:
            pass

        ## Only draws the cue when all balls are stationary
        # Respots any colored balls when all balls are stationary
        

        if not ball_moving:
            try:
                if not ball_in_hand:    
                    cue.draw(my_win,cue_ball.p.x, cue_ball.p.y)
            except NameError:
                pass
            for r in respot_list:
                if r.value == -4:   
                    cue_ball = r
                else:
                    balls.append(r)
            respot_list.clear()

        ## Checks if the cueball has collided with a pocket
        # If yes, creates a new cueball, sets the ball in hand condition and removes the old cueball from the game

        try:    
            white_potted = cue_ball.collide_pockets_cueball(pocket_list)
        except NameError:
            pass
        if white_potted:
            cue_ball_new = Cueball(cue_ball.spot_position.x, cue_ball.spot_position.y, 7, cue_ball.m,  cue_ball.color, 0,0, "cue", -4, Vector (cue_ball.spot_position.x, cue_ball.spot_position.y), True)
            respot_list.append(cue_ball_new)
            potted_balls.append(-4)
            del cue_ball
            white_potted = False
            ball_in_hand = True
            Foul = True

        ## Adds the scores of the potted balls to the current player's score
        # If any negative values in the potted balls list (fouls) these points are added to the opponent's tally

        if(len(potted_balls)) > 0:
            ball_potted = True
            for value in potted_balls:
                current_break.append(value)
                add_score(value,current_player,player1_Score, player2_Score)
                potted_balls.clear()

        ## Changes the current player iif a ball is not potted or a foul takes place
        # if the player changes the break is initialised to an empty list

        if not ball_moving and shot_played and (not ball_potted or Foul):
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
            shot_played = False
            ball_potted = False
            Foul = False
            current_break.clear()
        elif not ball_moving and shot_played and ball_potted:
            shot_played = False
            ball_potted = False
            print(current_break)

            ## Checks if the current break is bigger than any of the current high scores
            # if yes, adds that highscore to the file with the player's name and removes the one it replaces

            if current_player == 1:
                check_change_high_scores(HighScores, current_break, player1_Score)
            else:
                check_change_high_scores(HighScores, current_break, player2_Score)

            if len(balls) == 0:
                keepGoing = False
        
        ## Swap display

        pygame.display.update()
    
    my_win = pygame.display.set_mode((width,height))

    while not GameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOver = True

            elif event.type==pygame.KEYDOWN:

                ## Allows the user to play again if they press enter

                if event.key == 13:
                    run_game()


        ## Draw picture and update display
        my_win.fill(pygame.color.Color(cloth_color))

        ## Checks who has won the game
        # Checks for ties

        if player1_Score[1] > player2_Score[1]:
            winner = player1_Score
            tie = False
        elif player2_Score[1] > player1_Score[1]:
            winner = player2_Score
            tie = False
        else:
            tie = True

        font = pygame.font.Font(None, 25)

        ## Outputs the winner to screen
        # Outputs tie to the screen if the scores were even

        if not tie:
            text = font.render("Congratulations " + winner[0] + "! You win!", True, black)
            text2 = font.render("Press enter to play again or close the window to quit", True, black)
            text2_rect = text2.get_rect(center=(width/2, height/2+50))
            my_win.blit(text2,text2_rect)
        else:
            text = font.render("It's a tie! Press enter to play again or close the window to quit", True, black)
        text_rect = text.get_rect(center=(width/2, height/2))
        my_win.blit(text, text_rect)


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

def add_score(score, current_player, player1, player2):
    if score > 0:
        if current_player == 1:
            player1[1] += score
        else:
            player2[1] += score
    elif score < 0:
        if current_player == 1:
            player2[1] += abs(score)
        else:
            player1[1] += abs(score)

def find_high_scores(HighScores):

    ## Opens the high scores file
    # Splits lines by commas
    # Adds the scores to the HighScores list

    with open ('HighBreak.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(",")
            HighScores.append([line[0],int(line[1])])

def sort_high_scores(HighScores):

    ## Built in function to sort the scores in descending order

    HighScores.sort(reverse = True, key = lambda x: x[1])
    return (HighScores)

def check_change_high_scores(HighScores, CurrentBreak, CurrentPlayer):

    ## Checks if the current break should be added to the high scores list
    # If a new high score is added triggers a write to the file

    break_total = sum(CurrentBreak)
    ScoreAdded = False
    for Score in HighScores:
        if ScoreAdded == False:
            if break_total > Score[1]:
                HighScores.remove(HighScores[len(HighScores)-1])
                HighScores.append([CurrentPlayer[0],break_total])
                ScoreAdded = True

    sort_high_scores(HighScores)
    if ScoreAdded:
        write_high_scores(HighScores)

def write_high_scores(HighScores):

    ## Writes the high scores from the high scores list to file
    # Replaces everything already in the file due to opening with 'w'

    with open ('HighBreak.txt','w') as f:
        for Score in HighScores:
            f.write(Score[0] + ", " + str(Score[1]) + "\n")

## Start game
run_game()

