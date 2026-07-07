import pygame
import random

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

# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, WIDTH - 64)
enemyY = random.randint(50, 200)
enemyX_change = 0.3
enemyY_change = 30

# Enemy
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = HEIGHT - 84
bulletX_change = 0
bulletY_change = 0.5
bulletState = "ready"


def player(x, y) -> None:
    screen.blit(playerImg, (x, y))

def enemy(x, y) -> None:
    screen.blit(enemyImg, (x, y))

def fireBullet(x, y) -> None:
    global bulletState
    bulletState = "firing"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game loop
running = True
while running:
    screen.fill((40,40,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 0.3
            if event.key == pygame.K_d:
                playerX_change += 0.3
            if event.key == pygame.K_SPACE:
                fireBullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= WIDTH - 64:
        playerX = WIDTH - 64

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= WIDTH - 64:
        enemyX_change = -0.3
        enemyY += enemyY_change

    if bulletState == "firing":
        fireBullet(playerX, bulletY)    
        bulletY -= bulletY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()