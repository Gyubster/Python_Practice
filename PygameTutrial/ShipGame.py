import pygame

pygame.init()

display_width = 720
display_height = 480

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Lesson1')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
shipImg = pygame.image.load('ship.png')

def ship(x,y):
    game_display.blit(shipImg, (x, y))

x = (display_width*0.4)
y = (display_height*0.8)
x_change = 0
ship_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

# key pressed로도 구현 가능

    x += x_change

    game_display.fill(white)
    ship(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
