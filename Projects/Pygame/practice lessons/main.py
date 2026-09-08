import pygame
pygame.init()

HEIGHT = 480
WIDTH = 852

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Practice")

# Images
walkRight = [pygame.image.load(r'images and sounds/R1.png'), pygame.image.load(r'images and sounds/R2.png'), pygame.image.load(r'images and sounds/R3.png'), pygame.image.load(r'images and sounds/R4.png'), pygame.image.load(r'images and sounds/R5.png'), pygame.image.load(r'images and sounds/R6.png'), pygame.image.load(r'images and sounds/R7.png'), pygame.image.load(r'images and sounds/R8.png'), pygame.image.load(r'images and sounds/R9.png')]
walkLeft = [pygame.image.load(r'images and sounds/L1.png'), pygame.image.load(r'images and sounds/L2.png'), pygame.image.load(r'images and sounds/L3.png'), pygame.image.load(r'images and sounds/L4.png'), pygame.image.load(r'images and sounds/L5.png'), pygame.image.load(r'images and sounds/L6.png'), pygame.image.load(r'images and sounds/L7.png'), pygame.image.load(r'images and sounds/L8.png'), pygame.image.load(r'images and sounds/L9.png')]
bg = pygame.image.load(r'images and sounds/bg.jpg')
stand = pygame.image.load(r'images and sounds/standing.png')

# Score (hits)
score = 0

# Frames per second
clock = pygame.time.Clock()


def redrawGameWin():
    screen.blit(bg, (0,0 ))
    player1.draw(screen)
    goblin1.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    text = font.render('Score : ' + str(score), 1, (0,0,0))
    screen.blit(text, (5, 5))
    pygame.display.update()

def gameOver():
    font1 = pygame.font.Font('freesansbold.ttf', 100)
    text = font1.render('Game Over', 1, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - (text.get_width() // 2), HEIGHT // 2 - (text.get_height() // 2)))
    pygame.display.update()
    i = 0
    while i < 300:
        pygame.time.delay(10)
        i+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i == 301
                pygame.quit()

# Class for players (single or multiple)
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 18, self.y+10, 28, 55)

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 18, self.y+10, 28, 55)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y =  HEIGHT - 69
        self.walkCount = 0
        font1 = pygame.font.Font('freesansbold.ttf', 100)
        text = font1.render('-10', 1, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - (text.get_width() // 2), HEIGHT // 2 - (text.get_height() // 2)))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i == 301
                    pygame.quit()
# Projectiles
class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
# Enemies
class Enemy:
    walkRight = [pygame.image.load('images and sounds/R1E.png'), pygame.image.load('images and sounds/R2E.png'), pygame.image.load('images and sounds/R3E.png'), pygame.image.load('images and sounds/R4E.png'), pygame.image.load('images and sounds/R5E.png'), pygame.image.load('images and sounds/R6E.png'), pygame.image.load('images and sounds/R7E.png'), pygame.image.load('images and sounds/R8E.png'), pygame.image.load('images and sounds/R9E.png'), pygame.image.load('images and sounds/R10E.png'), pygame.image.load('images and sounds/R11E.png')]
    walkLeft = [pygame.image.load('images and sounds/L1E.png'), pygame.image.load('images and sounds/L2E.png'), pygame.image.load('images and sounds/L3E.png'), pygame.image.load('images and sounds/L4E.png'), pygame.image.load('images and sounds/L5E.png'), pygame.image.load('images and sounds/L6E.png'), pygame.image.load('images and sounds/L7E.png'), pygame.image.load('images and sounds/L8E.png'), pygame.image.load('images and sounds/L9E.png'), pygame.image.load('images and sounds/L10E.png'), pygame.image.load('images and sounds/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end] 
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0 
            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(screen, (0, 128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        
        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        
    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False


font = pygame.font.Font('freesansbold.ttf', 20)
player1 = Player(WIDTH // 2, HEIGHT - 69, 64, 64)
shootLoop = 0
bullets:list[Projectile] = []
goblin1 = Enemy(100, HEIGHT - 64, 64, 64, WIDTH - 64)

# main loop
running = True
while running:
    clock.tick(27)

    if goblin1.visible:
        if player1.hitbox[1]< goblin1.hitbox[1] + goblin1.hitbox[3] and player1.hitbox[1] + player1.hitbox[3]> goblin1.hitbox[1]:
            if player1.hitbox[0] + player1.hitbox[2]> goblin1.hitbox[0] and player1.hitbox[0] < goblin1.hitbox[0] + goblin1.hitbox[2]:
                player1.hit()
                score -= 10
    elif not goblin1.visible:
        gameOver()
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if shootLoop > 0:
        shootLoop += 1
    
    if shootLoop > 3:
        shootLoop = 0

    for bullet in bullets:
        if goblin1.visible:
            if bullet.y - bullet.radius < goblin1.hitbox[1] + goblin1.hitbox[3] and bullet.y + bullet.radius > goblin1.hitbox[1]:
                if bullet.x + bullet.radius > goblin1.hitbox[0] and bullet.x - bullet.radius < goblin1.hitbox[0] + goblin1.hitbox[2]:
                    goblin1.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        if bullet.x < WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if player1.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2), 5, (0,0,0), facing))

        shootLoop += 1
    if keys[pygame.K_a]:
        if player1.x >= 5:
            player1.left = True
            player1.right = False
            player1.x -= player1.vel
            player1.standing = False
    elif keys[pygame.K_d]:
        if player1.x <= WIDTH - 69:
            player1.left = False
            player1.right = True
            player1.x += player1.vel
            player1.standing = False 
    else:
        player1.standing = True
        player1.walkCount = 0
    
    
    if not player1.isJump:

        if keys[pygame.K_w]:
            player1.isJump = True
            player1.right = False
            player1.left = False
            player1.walkCount = 0
    
    else:
        if player1.jumpCount >= -10:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1
        else:
            player1.isJump = False
            player1.jumpCount = 10
    redrawGameWin()
    
pygame.quit()