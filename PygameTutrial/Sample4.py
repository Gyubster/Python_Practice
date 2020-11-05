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

class Player1():
    def __init__(self):
        super().__init__()
        rect = pygame.Rect((0, 0), (32, 32))
        main = pygame.Surface((30, 30))
        main.fill(BLACK)


while not Done:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.ACTIVEEVENT:
            Flag ^= True
        elif event.type == pygame.QUIT:
            Done = True
    Screen.fill(WHITE)

    if Flag == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player1.rect.move_ip(0, -2)
            elif event.key == pygame.K_DOWN:
                Player1.rect.move_ip(0, 2)
            elif event.key == pygame.K_LEFT:
                Player1.rect.move_ip(-2, 0)
            elif event.key == pygame.K_RIGHT:
                Player1.rect.move_ip(2, 0)
        pygame.draw.rect(Screen, RED, [0, 0, 30, 30], 2)
        pygame.draw.rect(Screen, BLUE, [690, 450, 30, 30], 2)
        Screen.blit(Player1.main, Player1.rect)

    # Print Message If User Mouse Is In Outside.
    else:
        textSurface = font.render('Pause', True, pygame.Color('BLACK'), None)
        textRect = textSurface.get_rect()
        textRect = (360, 240)
        Screen.blit(textSurface, textRect)

    pygame.display.flip()

pygame.quit()