import pygame
import os
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(group)
        self.image = bomb_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.boomed = False

    def get_click(self, position):
        x_pos, y_pos = position
        boomed = False
        if (self.rect.top <= y_pos <= self.rect.bottom and not self.boomed and
                self.rect.left <= x_pos <= self.rect.right):
            self.boom()
            boomed = True
        return boomed

    def boom(self):
        self.image = boom_image
        position = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.boomed = True


def create_bombs():
    bombs = list()
    for i in range(amount_bombs):
        width, height = bomb_image.get_rect().size
        x_coord, y_coord = random.randrange(screen_size[0] - width), random.randrange(screen_size[1] - height)
        bombs.append(Bomb(x_coord, y_coord, all_sprites))
    return bombs


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
white = pygame.Color('white')
game_on, amount_bombs = True, 20
all_sprites = pygame.sprite.Group()
bomb_image = load_image('bomb.png')
boom_image = load_image('boom.png')
bombs = create_bombs()

while game_on:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in bombs:
                if bomb.get_click(event.pos):
                    break

    all_sprites.draw(screen)
    pygame.display.flip()
