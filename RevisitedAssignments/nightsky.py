import pygame
import random
import math

class Vector:

    x = 0
    y = 0

    def __init__ (self, x, y):
        self.x = float(x)
        self.y = float(y)

class Star():

    r = 0
    x = 0
    y = 0

    def __init__ (self, radius, x_position, y_position):
        self.r = radius
        self.x = x_position
        self.y = y_position

class ShootingStar(Star):

    v = Vector(0,0)

    distance = 0

    def __init__ (self, radius, x_position, y_position, velocity, distance):
        self.r = radius
        self.x = x_position
        self.y = y_position
        self.v = velocity
        self.d = distance

def run_game():

    # Initialize pygame and set up the display window.
    pygame.init()

    width = 700
    height = 500

    StarSky = pygame.display.set_mode((width, height))

    star_number = random.randint(70,130)

    stars = []
    shooting_stars = []

    color = pygame.color.Color("Yellow")

    clock = pygame.time.Clock()

    for i in range(0, star_number):
        s = Star(random.randint(1,4),random.randint(0,700),random.randint(0,500))
        stars.append(s)

        

    # The game loop starts here.
    keep_going = True
    while (keep_going):

        # 1. Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False


        # 2. Apply rules of game world
        # None currently

        # 3. Simulate the world
        # None currently

        # 4. Draw frame
        # Draw Background
        StarSky.fill(pygame.color.Color("black"))
        # Draw ball
        for s in stars:
            pygame.draw.circle(StarSky, color, (s.x, s.y), s.r)
    

        for s in shooting_stars:
            x,y = s.v
            s.x += x
            s.y += y
            s.d -= 1
            pygame.draw.circle(StarSky, color, (s.x, s.y), s.r)
            if s.d == 0:
                shooting_stars.remove(s)
            

        Shooting = random.randint(0,300)
        if Shooting == 0:
            SStar = ShootingStar(random.randint(1,4),random.randint(0,700),random.randint(0,500),(random.uniform(-1,1) * 5 , random.uniform(-1,1) * 3), random.randint(40,70))
            shooting_stars.append(SStar)

        clock.tick(60)
        
        # Swap display
        pygame.display.update()

    # The game loop ends here.

    pygame.quit()


# Start game
run_game()