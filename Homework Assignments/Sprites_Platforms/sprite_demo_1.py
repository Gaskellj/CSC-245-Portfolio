"""

Author: John Rieffel

Based off of 

Simpson College Computer Science Material

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

from player import Player
from simple_platform import Box

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    HEIGHT = 480
    WIDTH = 640
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)

    jumping = False


    pygame.display.set_caption("demo with sprite sheets")

    active_sprite_list = pygame.sprite.Group()
    # Create the player
    player = Player()
    platform = Box(pygame.color.Color("blue"),50,50) 
    platform.rect.x = 400
    platform.rect.y = HEIGHT - platform.rect.h

    platform2 = Box(pygame.color.Color("green"),50,50) 
    platform2.rect.x = 250
    platform2.rect.y = HEIGHT - platform.rect.h

    platform3 = Box(pygame.color.Color("orange"),50,50) 
    platform3.rect.x = 300
    platform3.rect.y = HEIGHT - 2*(platform.rect.h)

    # Create all the levels

    player.rect.x = 100 
    player.rect.y = HEIGHT - player.rect.height
    active_sprite_list.add(player,platform,platform2,platform3)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP and jumping == False:
                    player.jump()
                    jumping = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    player.stop_x()
                if event.key == pygame.K_RIGHT:
                    player.stop_x()

        # Update the player.
        active_sprite_list.update()

        if pygame.sprite.collide_rect(player,platform) or pygame.sprite.collide_rect(player,platform2) or pygame.sprite.collide_rect(player,platform3):
            player.stop_x()
            player.stop_y()
            jumping = False

        if jumping:
            player.gravity()

        if player.rect.bottom >= 480:
            player.stop_y()
            jumping = False



        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        #current_level.draw(screen)
        screen.fill(pygame.color.Color("gray14")) 
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
