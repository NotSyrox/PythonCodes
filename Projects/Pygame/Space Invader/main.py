import pygame
from pygame import mixer
import random

# Initialize Pygame
pygame.init()

HEIGHT = 600
WIDTH = 800

# Creates the Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 0.5 * WIDTH - 32
playerY = HEIGHT - 84
playerX_change = 0

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10

gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
# Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numberOfEnemies = 5

for _ in range(numberOfEnemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, WIDTH - 64))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(0.2)
    enemyY_change.append(30)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = HEIGHT - 84
bulletX_change = 0
bulletY_change = 0.5
bulletState = "ready"


def showScore(x, y):
    acutalScore = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(acutalScore, (x, y))

def gameOverText():
    overText = gameOverFont.render("GAME OVER", True, (255,255,255))
    screen.blit(overText, (200, 250))

def player(x, y) -> None:
    screen.blit(playerImg, (x, y))

def enemy(x, y, i) -> None:
    screen.blit(enemyImg[i], (x, y))

def fireBullet(x, y) -> None:
    global bulletState
    bulletState = "firing"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY) -> bool:
    distance = (((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2)) ** 0.5
    return True if distance < 27 else False


# Game loop
running = True
while running:
    screen.fill((40,40,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 0.2
            if event.key == pygame.K_d:
                playerX_change += 0.2
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= WIDTH - 64:
        playerX = WIDTH - 64

    for i in range(numberOfEnemies):
        if enemyY[i] >= playerY - 64:
            for j in range(numberOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= WIDTH - 64:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    
        if collision:
            explosionSound = mixer.Sound('explosion.wav')
            explosionSound.play()
            bulletY = 0
            bulletState = "ready"
            score += 1
            enemyX[i] = random.randintenemyX = random.randint(0, WIDTH - 64)
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = HEIGHT - 74
        bulletState = "ready"

    if bulletState == "firing":
        fireBullet(bulletX, bulletY)    
        bulletY -= bulletY_change

    

    player(playerX,playerY)
    showScore(textX, textY)
    pygame.display.update()