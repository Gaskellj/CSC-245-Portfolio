"""

Author: John Rieffel

Based off of 

Simpson College Computer Science Material

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

from turtle import heading, width
import pygame
from moving_ball_2d import MovingBall

from player import Player
from Launcher import launcher
from vector import Vector

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    HEIGHT = 480
    WIDTH = 800
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("demo with sprite sheets")

    active_sprite_list = pygame.sprite.Group()
    # Create the player
    player = Player()

    # Create all the levels

    player.rect.x = 50
    player.rect.y = HEIGHT - player.rect.height
    active_sprite_list.add(player)

    Launcher = launcher(0,0, 50, (0,100,0))

    ball = MovingBall(WIDTH-200, HEIGHT - player.rect.height,7,1.0,(0,100,0), 0,0)

    ball_moving = False

    #Loop until the user clicks the close button.
    done = False
    won = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                    start = Vector(ball.p.x, ball.p.y)
                    x, y = pygame.mouse.get_pos()
                    end = Vector(x ,y)
                    start -= end
                    dist = start.length()
                    start.normalize()
                    force = dist/20.0
                    if force > 10:
                        force = 10
                
                    start *= force
                    ball.v = start
                    ball_moving = True

        # Update the player.
        active_sprite_list.update()



        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        #current_level.draw(screen)
        screen.fill(pygame.color.Color("gray14")) 
        active_sprite_list.draw(screen)

        if not ball_moving:   
            Launcher.draw(screen,ball.p.x, ball.p.y)
        else:
            ball.simulate(WIDTH,HEIGHT)
        
        ball.draw(screen)

        #if ball.collide_sprite(active_sprite_list):
            #pass


        if ball.p.y > HEIGHT:
            del ball
            ball = MovingBall(WIDTH-200, HEIGHT - player.rect.height,7,1.0,(0,100,0), 0,0)
            ball_moving = False



        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

        while won:

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    won = False # Flag that we are done so we exit this loop


            screen.fill(pygame.color.Color("gray14")) 

            clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()

