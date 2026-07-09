import pygame
pygame.init()

HEIGHT = 500
WIDTH = 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption("Pygame Practice")

x = WIDTH / 2 
y = HEIGHT - 50
width = 40
height = 60
velocity = 5

isJump = False
jumpCount = 10

running = True
while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if x >= 5:
            x -= velocity
    if keys[pygame.K_d]:
        if x <= WIDTH - 45:
            x += velocity
    if not isJump:

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0),(x, y, width, height))
    pygame.display.update()
pygame.quit()