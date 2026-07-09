import pygame
pygame.init()

HEIGHT = 480
WIDTH = 852
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame Practice")

walkRight = [pygame.image.load(r'images and sounds/R1.png'), pygame.image.load(r'images and sounds/R2.png'), pygame.image.load(r'images and sounds/R3.png'), pygame.image.load(r'images and sounds/R4.png'), pygame.image.load(r'images and sounds/R5.png'), pygame.image.load(r'images and sounds/R6.png'), pygame.image.load(r'images and sounds/R7.png'), pygame.image.load(r'images and sounds/R8.png'), pygame.image.load(r'images and sounds/R9.png')]
walkLeft = [pygame.image.load(r'images and sounds/L1.png'), pygame.image.load(r'images and sounds/L2.png'), pygame.image.load(r'images and sounds/L3.png'), pygame.image.load(r'images and sounds/L4.png'), pygame.image.load(r'images and sounds/L5.png'), pygame.image.load(r'images and sounds/L6.png'), pygame.image.load(r'images and sounds/L7.png'), pygame.image.load(r'images and sounds/L8.png'), pygame.image.load(r'images and sounds/L9.png')]
bg = pygame.image.load(r'images and sounds/bg.jpg')
char = pygame.image.load(r'images and sounds/standing.png')

clock = pygame.time.Clock()

x = WIDTH / 2 
y = HEIGHT - 69
width = 64
height = 64
velocity = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWin():
    global walkCount
    screen.blit(bg, (0,0 ))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1

    elif right:
        screen.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
    pygame.display.update()

running = True
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if x >= 5:
            left = True
            right = False
            x -= velocity
    elif keys[pygame.K_d]:
        if x <= WIDTH - 69:
            left = False
            right = True
            x += velocity
    else:
        right = False
        left = False
        walkCount = 0
    if not isJump:

        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    redrawGameWin()
    
pygame.quit()