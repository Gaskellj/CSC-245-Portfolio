import pygame, random
import time

def night_sky():

    pygame.init()

    width = 700
    height = 500

    StarSky = pygame.display.set_mode((width, height))

    StarSky.fill(pygame.color.Color("black"))

    star_number = random.randint(70,130)

    color = pygame.color.Color("Yellow")

    for x in range(0, star_number):
        x = random.randint(0,700)
        y = random.randint(0,500)

        radius = random.randint(1,4)

        pygame.draw.circle(StarSky, color, (x, y), radius)

        pygame.display.update()
        
    keep_going = True
    while (keep_going):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            
        time.sleep(random.randint(3,7))
        
        x = random.randint(50,650)
        y = random.randint(50,450)

        radius = random.randint(1,4)

        direction_x = random.randint(-10,10)/10
        direction_y = random.randint(-10,10)/10

        for i in range(0,random.randint(200,400)):
            x = x + direction_x
            y = y + direction_y
            pygame.draw.circle(StarSky, color, (x,y), radius)
            pygame.display.update()
            time.sleep(0.01)
            pygame.draw.circle(StarSky, pygame.color.Color("black"), (x-(direction_x)*30,y-(direction_y)*30), radius+1)
            pygame.display.update()

        for z in range(0,31):
            pygame.draw.circle(StarSky, pygame.color.Color("black"), (x-(direction_x)*30,y-(direction_y)*30), radius+1)
            x = x + direction_x
            y = y + direction_y
            pygame.display.update()
            time.sleep(0.01)
        
    pygame.quit()

night_sky()
