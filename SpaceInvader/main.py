import pygame
import random
import math
from pygame import mixer

# Intialize the pygame:
pygame.init()

screen=pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Space Invador:")
icon=pygame.image.load("SpaceInvader/rocket.png")
pygame.display.set_icon(icon)

# Background:
image = pygame.image.load("SpaceInvader/back.png")
background = pygame.transform.scale(image, (800, 600))

# Background Music:
mixer.music.load("SpaceInvader/Background.mp3")
mixer.music.play(-1)

# Player:
playerImg=pygame.image.load("SpaceInvader/spaceship.png")
playerX=370
playerY=490
playerX_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))
    
# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("SpaceInvader/ufo.png"))
    enemyX.append(random.randint(0, 725))
    enemyY.append(random.randint(10, 200))
    enemyX_change.append(0.3)
    enemyY_change.append(50)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Bullet:
bulletImg = pygame.image.load("SpaceInvader/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2   # speed of bullet
bullet_state = "ready"


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    
    if distance <25:
        return True
    else:
        return False

# score:
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# Game Over text
game_over = False
over_font=pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(250,250))

# GAME LOOP:
running=True
while running:
    # Background color:
    screen.fill((0,0,0))
    
    # Background image:
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.5
                print("Left aerrow:")
            if event.key==pygame.K_RIGHT:
                playerX_change=0.5
                print("Right aerrow:")
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
                print("Key releaseed:")
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound("SpaceInvader/bulletSound.mp3")
                    bullet_sound.play()
                    # get the x cordinate of spaceship
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                    
    # moving of spaceship:
    playerX+=playerX_change
    # making boundries:
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    
    player(playerX,playerY)
    
    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        
        # if enemy hit spaceship
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            if not game_over:
                game_over_sound = mixer.Sound("SpaceInvader/GameOver.mp3")
                game_over_sound.play()
                game_over = True  
            break
            
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
            
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX + 16, bulletY + 10)
        if collision:
            exploision_sound=mixer.Sound("SpaceInvader/exploid.mp3")
            exploision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value+= 1
            print("Score:", score_value)
            enemyX[i] = random.randint(0,725)
            enemyY[i] = random.randint(10,200)

        enemy(enemyX[i], enemyY[i], i)
            
    # bullet movement:
    # bullet reset
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
        
        # bullet shooting
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    
    show_score(textX,textY) 
    if game_over:
        game_over_text()
    pygame.display.update()