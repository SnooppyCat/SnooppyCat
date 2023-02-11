import pygame
import random
from pygame. constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

TIME = pygame.time.Clock()
GREEN = 1, 255, 4

window = width, height = 800, 600

main_surface = pygame.display.set_mode(window)
ball = pygame.Surface((20, 20))
ball_rect = ball.get_rect()
ball_speed = 3
ball.fill((155, 155, 155))

def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill((255, 0, 0))
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = 1
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = 1
    return [bonus, bonus_rect, bonus_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

enemies = []
bonuses = []



working = True
while working:
    TIME.tick(350)
    for event in pygame.event.get():
        if event.type == QUIT:
            working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())   

    

    pressed_keys = pygame.key.get_pressed()

    main_surface.fill((255, 237, 109))
    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        enemy[1]=enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))
    
    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))

    


    if pressed_keys[K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move(0, ball_speed)
    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)
    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)
    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    print(len(enemies))



    pygame.display.flip()