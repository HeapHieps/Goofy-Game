import pygame
import math
import random


#Surface
pygame.init()
screen = pygame.display.set_mode((1345,600))
pygame.display.set_caption('The Longer We Live')
logo = pygame.image.load('LIVE JOHNNY REACTION.png')
pygame.display.set_icon(logo)
background = pygame.image.load('LastStand.png')
score = 0

#Ingame characters
Cente = pygame.image.load('CENTEs.png')
Cente_img = pygame.transform.scale(Cente,(100,100))
playerX = 1100
playerY = 300
playerX_Movement = 0
PlayerY_change = 0

Neco = pygame.image.load('long_neco_arc.png')
Neco_img = pygame.transform.scale(Neco,(75,115))

Neco_img = []
NecoX = []
NecoY = []
NecoXMovement = []
NecoYMovement = []
num_of_Necos = 5
for i in range(num_of_Necos):
    Neco = pygame.image.load('long_neco_arc.png')
    Neco_img.append(pygame.transform.scale(Neco,(75,115)))
    NecoX.append(random.randint(-40,-10))
    NecoY.append(random.randint(130,350))
    NecoXMovement.append(.2)
    NecoYMovement.append(0)


bullet = pygame.image.load("bulletv.png")
bullet_img = pygame.transform.scale(bullet,(35,35))
bullet_img = pygame.transform.rotate(bullet_img,180)
bulletX = 0
bulletY= 0
bulletX_Movement = 2
bulletY_Movement = 0
bullet_state = "ready"

def NecoArc(x,y,i):
    screen.blit(Neco_img[i],(x,y))

def player(x,y):
    screen.blit(Cente_img,(x,y))

def bulletv(x,y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bullet_img,(x,y+38))

def collisionDec(NecoX,NecoY,bulletX,bulletY):
    distance = math.sqrt((math.pow(NecoX - bulletX,2)) + (math.pow(NecoY - bulletY,2)))
    if distance <40:
        return True
    else:
        return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Movement = -.7
            if event.key == pygame.K_RIGHT:
                playerX_Movement = .7
            if event.key == pygame.K_UP:
                PlayerY_change = -.7
            if event.key == pygame.K_DOWN:
                PlayerY_change = .7
        if event.type == pygame.KEYUP: #Checking if the key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Movement = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_change = 0
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX 
                    bulletY = playerY
                    bulletv(bulletX,bulletY)
    if playerX <= 1050:
        playerX = 1050
    if playerX >=1200:
        playerX = 1200
    if playerY <= 120:
        playerY = 120
    if playerY >= 425:
        playerY = 425
    
    screen.blit(background,(0,0))

    playerX += playerX_Movement
    playerY += PlayerY_change

    NecoX[i] += NecoXMovement[i]
    
    if bullet_state =="fired":
        bulletv(bulletX,bulletY)
        bulletX -=bulletX_Movement
        bulletY -= bulletY_Movement
    if bulletX <= 0:
        bullet_state = "ready"
    
    for i in range(num_of_Necos):
        NecoX[i] += NecoXMovement[i]
        
        collision = collisionDec(NecoX[i],NecoY[i],bulletX,bulletY)
        if collision:
            bulletX = 0
            bulletY = 0
            score += 1
            print(score)
            NecoX[i] = random.randint(-40,-10)
            NecoY[i] = random.randint(145,350)
        NecoArc(NecoX[i],NecoY[i], i)
    
    player(playerX,playerY)

    

    pygame.display.update()
