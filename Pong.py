import pygame
from sys import exit
import random
pygame.init()

display = pygame.display.set_mode((750, 250))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

logo = pygame.image.load("Sprites/Pong.jpg")
pygame.display.set_icon(logo)

background = pygame.Surface((750, 250))

background.fill("Black")

playerEntity = pygame.Surface((10, 50))
playerEntity_detecBox = playerEntity.get_rect(topleft = (75, 100))
playerEntity.fill("White")

player_Score = 0

playerEntity_score = pygame.font.Font(None, 50)
playerEntity_score_text = playerEntity_score.render(str(player_Score), False, "White")

playerEntityB = pygame.Surface((10, 50))
playerEntityB_detecBox = playerEntityB.get_rect(topleft = (650, 100))
playerEntityB.fill("White")

playerB_Score = 0

playerEntityB_score = pygame.font.Font(None, 50)
playerEntityB_score_text = playerEntityB_score.render(str(playerB_Score), False, "White")

ballEntity = pygame.Surface((10, 10))
ballEntity_detecBox = ballEntity.get_rect(topleft = (350, 100))
ballEntity.fill("White")
MovementLeft = True
y_movement = random.randint(-2, 2)
SwungTrajectory = False
FixedTrajectory_UP = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    display.blit(background, (0, 0))

    display.blit(playerEntity, playerEntity_detecBox)

    display.blit(playerEntityB, playerEntityB_detecBox)

    display.blit(playerEntity_score_text, (10, 110))

    display.blit(playerEntityB_score_text, (720, 110))

    display.blit(ballEntity, ballEntity_detecBox)

    if ballEntity_detecBox.left == playerEntity_detecBox.right and playerEntity_detecBox.top < ballEntity_detecBox.bottom and playerEntity_detecBox.bottom > ballEntity_detecBox.top:
        y_movement = random.randint(-2, 2)
        print("Collision - P: A")
        MovementLeft = False
        SwungTrajectory = True

    if ballEntity_detecBox.right == playerEntityB_detecBox.left and playerEntityB_detecBox.top < ballEntity_detecBox.bottom and playerEntityB_detecBox.bottom > ballEntity_detecBox.top:
        y_movement = random.randint(-2, 2)
        print(y_movement)
        print("Collision - P: B")
        MovementLeft = True
        SwungTrajectory = True

    if SwungTrajectory == True:
        ballEntity_detecBox.top = ballEntity_detecBox.top + y_movement
    elif SwungTrajectory == False:
        if FixedTrajectory_UP == True:
            ballEntity_detecBox.top = ballEntity_detecBox.top - 2
        elif FixedTrajectory_UP == False:
            ballEntity_detecBox.top = ballEntity_detecBox.top + 2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerEntity_detecBox.top -= 2
    elif keys[pygame.K_s]:
        playerEntity_detecBox.top += 2

    if keys[pygame.K_UP]:
        playerEntityB_detecBox.top -= 2
    if keys[pygame.K_DOWN]:
        playerEntityB_detecBox.bottom += 2

    if playerEntity_detecBox.top < 0:
        playerEntity_detecBox.top = 0
    elif playerEntity_detecBox.bottom > 250:
        playerEntity_detecBox.bottom = 250

    if playerEntityB_detecBox.top < 0:
        playerEntityB_detecBox.top = 0
    elif playerEntityB_detecBox.bottom > 250:
        playerEntityB_detecBox.bottom = 250

    print(ballEntity_detecBox.bottom)

    if ballEntity_detecBox.top <= 0:
        print("Ball Collision - Top")
        SwungTrajectory = False
        FixedTrajectory_UP = False
    elif ballEntity_detecBox.bottom >= 250:
        print("Ball Collision - Bottom")
        SwungTrajectory = False
        FixedTrajectory_UP = True

    if MovementLeft == True:
        ballEntity_detecBox.left -= 5
    elif MovementLeft == False:
        ballEntity_detecBox.left += 5

    if ballEntity_detecBox.right == 850:
        player_Score += 1
        playerEntity_score_text = playerEntity_score.render(str(player_Score), False, "White")
        MovementLeft = False
        ballEntity_detecBox.right = 365
    elif ballEntity_detecBox.left == -100:
        playerB_Score += 1
        playerEntityB_score_text = playerEntityB_score.render(str(playerB_Score), False, "White")
        MovementLeft = True
        ballEntity_detecBox.right = 365

    pygame.display.update()
    clock.tick(60)
