import pygame

# pygame boilerplate
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# game loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # update
    # draw
    pygame.display.update()
    clock.tick(60)
