import pygame
import csv
from Objects import *
from Drawer import *
from levels import levels

pygame.init()
window = pygame.display.set_mode((800, 600))
run = True
pygame.display.set_caption("First Try")
MainPlayer = Player([20, 20], "Assets/Hero/Base", "Base.png", [24, 24])
clock = pygame.time.Clock()
levels[0].curr = True
currentLevel = -1
for i in levels:
    if i.curr == True:
        currentLevel = i
        MainPlayer.coords = currentLevel.player_start_pos[0]

objs = currentLevel.objs
solobjs = currentLevel.solobjs
objs.append(MainPlayer)
while run:
    clock.tick(60)



    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for obj in objs:
        Drawer().draw(obj.coords, window, obj.sprite_path, obj.sprite_name)
    can_move_right, can_move_left, can_move_down, can_move_up = True, True, True, True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        for obj in solobjs:
            if MainPlayer.coords[1] + MainPlayer.hitbox[1] - MainPlayer.speed in range(obj.coords[1],
                                                                                           obj.coords[1] + obj.hitbox[
                                                                                               1]) or MainPlayer.coords[
                    1] + MainPlayer.speed in range(obj.coords[1], obj.coords[1] + obj.hitbox[1]):
                    if MainPlayer.coords[0] + MainPlayer.hitbox[0] + 10 - MainPlayer.speed in range(obj.coords[0],
                                                                                               obj.coords[0] +
                                                                                               obj.hitbox[0]):
                        can_move_right = False
        if can_move_right:
            MainPlayer.moving(-1)

    if keys[pygame.K_LEFT]:
        for obj in solobjs:
                if MainPlayer.coords[1] + MainPlayer.hitbox[1] - MainPlayer.speed in range(obj.coords[1],
                                                                                           obj.coords[1] + obj.hitbox[
                                                                                               1]) or MainPlayer.coords[
                    1] + MainPlayer.speed in range(obj.coords[1], obj.coords[1] + obj.hitbox[1]):
                    if MainPlayer.coords[0] - MainPlayer.hitbox[0] / 2 + MainPlayer.speed in range(obj.coords[0],
                                                                        obj.coords[0] +
                                                                        obj.hitbox[0]):
                        can_move_left = False
        if can_move_left:
            MainPlayer.moving(1)

    if keys[pygame.K_DOWN]:
        for obj in solobjs:
            if obj != MainPlayer:
                if MainPlayer.coords[0] + MainPlayer.hitbox[0] - MainPlayer.speed in range(obj.coords[0],
                                                                                           obj.coords[0] + obj.hitbox[
                                                                                               0]) or MainPlayer.coords[
                    0] + MainPlayer.speed in range(obj.coords[0], obj.coords[0] + obj.hitbox[0]):
                    if MainPlayer.coords[1] + MainPlayer.hitbox[1] + 10 - MainPlayer.speed in range(obj.coords[1],
                                                                                               obj.coords[1] +
                                                                                               obj.hitbox[1]):
                        can_move_down = False
        if can_move_down:
            MainPlayer.flight(-1)

    if keys[pygame.K_UP]:
        for obj in solobjs:
            if obj != MainPlayer:
                if MainPlayer.coords[0] + MainPlayer.hitbox[0] - MainPlayer.speed in range(obj.coords[0],
                                                                                           obj.coords[0] + obj.hitbox[
                                                                                               0]) or MainPlayer.coords[
                    0] + MainPlayer.speed in range(obj.coords[0], obj.coords[0] + obj.hitbox[0]):
                    if MainPlayer.coords[1] - MainPlayer.hitbox[1] / 2 + MainPlayer.speed in range(obj.coords[1],
                                                                                                   obj.coords[1] +
                                                                                                   obj.hitbox[1]):
                        can_move_up = False
        if can_move_up:
            MainPlayer.flight(1)

    pygame.display.update()

pygame.quit()
