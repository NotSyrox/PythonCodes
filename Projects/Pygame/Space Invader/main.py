import pygame

# Initialize Pygame
pygame.init()

HEIGHT = 600
WIDTH = 800

# Creates the Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 0.5 * WIDTH - 32
playerY = HEIGHT - 84
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    screen.fill((50,50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 0.3
            if event.key == pygame.K_d:
                playerX_change += 0.3

            if event.key == pygame.K_w:
                playerY_change -= 0.3
            if event.key == pygame.K_s:
                playerY_change += 0.3
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
        
    playerX += playerX_change
    playerY += playerY_change

    player(playerX,playerY)
    pygame.display.update()