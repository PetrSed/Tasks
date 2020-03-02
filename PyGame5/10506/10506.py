import pygame
import os

pygame.init()
sc = pygame.display.set_mode((600, 300))
clock, step = pygame.time.Clock(), 1
fullname = os.path.join('data', 'gameover.png')
picture = pygame.image.load(fullname).convert()
now_x, blue = -600, pygame.Color('blue')


def draw_picture():
    sc.blit(picture, (now_x, 0))
    pygame.display.update()


pygame.display.update()

game_on = True
sc.fill(blue)
while game_on:
    sc.fill(blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    if now_x != 0:
        now_x += step
    draw_picture()
    pygame.display.flip()
    clock.tick(200)
