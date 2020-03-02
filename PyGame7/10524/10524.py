import pygame
import os
import sys

pygame.init()
screen_size = width, height = 600, 600
screen = pygame.display.set_mode(screen_size)
black = pygame.Color('black')
screen.fill(black)


def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


tile_images = {"wall": load_image("box.png"), "empty": load_image("grass.png")}
player_image = load_image("mar.png", -1)
tile_width = tile_height = 50


def load_level(filename):
    filename = "data/" + filename
    with open(filename, "r") as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    if max_width < 12:
        max_width = 12
    return list(map(lambda x: x.ljust(max_width, "."), level_map))


def terminate():
    pygame.quit()
    sys.exit()


def menu():
    background = load_image('start_back.png')
    screen.blit(background, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Tile("empty", x, y)
            elif level[y][x] == "#":
                Tile("wall", x, y)
            elif level[y][x] == "@":
                Tile("empty", x, y)
                new_player = Player(x, y)
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        if tile_type != "wall":
            super().__init__(all_sprites)
        else:
            super().__init__(tile_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

    def moving(self, vx, vy):
        self.rect.x = (self.rect.x + vx) % width
        self.rect.y = (self.rect.y + vy) % height


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = width // 2 - (target.rect.x + target.rect.w // 2)
        self.dy = height // 2 - (target.rect.y + target.rect.h // 2)


menu()
player = None
all_sprites = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player, level_x, level_y = generate_level(load_level("first.txt"))
step_x, step_y = 0, 0
moving, running = False, True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            moving = False
            step_y = 0
            step_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                step_y -= 1
            if event.key == pygame.K_RIGHT:
                step_x += 1
            if event.key == pygame.K_DOWN:
                step_y += 1
            if event.key == pygame.K_LEFT:
                step_x -= 1
        moving = True
    if moving:
        player.moving(step_x, step_y)
        if pygame.sprite.spritecollideany(player, tile_group):
            player.moving(-step_x, -step_y)
    all_sprites.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
