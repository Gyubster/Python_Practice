import pygame

# Initializing pygame
pygame.init()

# Colors
BLACK = (0,  0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Basics
Size = [720, 480]
Screen = pygame.display.set_mode(Size)
font= pygame.font.SysFont("consolas",20)
pygame.display.set_caption("Sample3")

# Loop setting
Done = False
Flag = True
Clock = pygame.time.Clock()

while not Done:
    Clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.ACTIVEEVENT:
            Flag ^= True
        elif event.type == pygame.QUIT:
            Done = True
    Screen.fill(WHITE)
    # Drawing House If User Mouse Is In Display.
    if Flag == True:
        pygame.draw.circle(Screen, BLUE, [60, 250], 40, 2)
        pygame.draw.circle(Screen, BLUE, [60, 100], 40)
        pygame.draw.rect(Screen, RED, [30, 30, 10, 10], 2)
        pygame.draw.rect(Screen, RED, [70, 30, 10, 10])

    # Print Message If User Mouse Is In Outside.
    else:
        textSurface = font.render('Pause', True, pygame.Color('BLACK'), None)
        textRect = textSurface.get_rect()
        textRect = (360, 240)

        Screen.blit(textSurface, textRect)

    pygame.display.flip()

pygame.quit()