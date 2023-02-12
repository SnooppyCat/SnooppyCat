import pygame
import random
from os import listdir
from pygame. constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

TIME = pygame.time.Clock()
GREEN = 1, 255, 4
WHITE = 255, 255, 255
BACKGROUND_RGB = 172, 156, 188

window = width, height = 800, 600

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(window)

IMGS_PATH = 'goose'

player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_speed = 3

def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = 1
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = 1
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), window)
bgx = 0
bgx2 = bg.get_width()
bgx_speed = 2


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)





scores = 0
enemies = []
bonuses = []



working = True
while working:
    TIME.tick(270)
    for event in pygame.event.get():
        if event.type == QUIT:
            working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    

    pressed_keys = pygame.key.get_pressed()


    bgx -= bgx_speed
    bgx2 -= bgx_speed

    if bgx < -bg.get_width():
        bgx = bg.get_width()

    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()

    main_surface.blit(bg, (bgx, 0))
    main_surface.blit(bg, (bgx2, 0))

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True, WHITE), (width - 30, 0))


    for enemy in enemies:
        enemy[1]=enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            working = False
            print('The game is over!\nTry again!')

       
    
    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1


    


    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)
    if pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)
    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)
    if pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move(-player_speed, 0)

    print(len(enemies))



    pygame.display.flip()