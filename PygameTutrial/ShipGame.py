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

ship_speed = 0
ship_width, ship_height = 177, 87

def ship(x,y):
    game_display.blit(shipImg, (x, y))

def game_loop():
    game_exit = False

    x = (display_width*0.4)
    y = (display_height*0.8)

    x_change = 0
    y_change = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        game_display.fill(white)
        ship(x, y)

        if x < 0 or x > display_width - ship_width:
            game_exit = True

        if y < 0 or y > display_height - ship_height:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
