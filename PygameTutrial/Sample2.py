import pygame

pygame.init()

BLACK = ( 0,  0,  0)
WHITE = (255,255,255)
BLUE = ( 0,  0,255)
GREEN = ( 0,255,  0)
RED = (255,  0,  0)

Size = [720, 480]
screen = pygame.display.set_mode(Size)
pygame.display.set_caption("Drawing")

Done = False
Clock = pygame.time.Clock()

while not Done:
    Clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

    # Flag that we are done so we exit this loop
    screen.fill(BLACK)
    pygame.draw.circle(screen, BLUE, [60, 250], 40, 2)
    pygame.draw.circle(screen, BLUE, [60, 100], 40)
    pygame.draw.rect(screen, RED, [30, 30, 10, 10], 2)
    pygame.draw.rect(screen, RED, [70, 30, 10, 10])
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
