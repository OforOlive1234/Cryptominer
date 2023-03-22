import pygame
import time

# pygame boilerplate
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()



#initialise variables
r_hue = 0
g_hue = 0
b_hue = 0

loading = True

for i in range(255):
    r_hue += 1
    g_hue += 1
    b_hue += 1
    screen.fill((r_hue, g_hue, b_hue))
    pygame.display.update()
    clock.tick(60)


# game loop
while True:
   
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill((r_hue, g_hue, b_hue))
    
    # make a game object


    # update
    # draw
    pygame.display.update()
    clock.tick(60)
