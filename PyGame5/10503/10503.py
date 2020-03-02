import pygame
import os


class Car(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.position = (1, 0)
        self.step = 1
        fullname = os.path.join('data', 'car2.png')
        self.car = pygame.image.load(fullname)
        self.screen = screen
        self.move = True

    def rotate(self):
        self.car = pygame.transform.flip(self.car, True, False)
        self.move = not self.move

    def update_position(self):
        x, y = self.position
        if x == 450 or x == 0:
            self.rotate()
        if self.move:
            self.position = (x + self.step, y)
        else:
            self.position = (x - self.step, y)

    def draw(self):
        self.screen.blit(self.car, self.position)


pygame.init()
screen = pygame.display.set_mode((600, 95))
clock = pygame.time.Clock()
white = pygame.Color('white')
game_on, speed = True, 200
car = Car(screen)

while game_on:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    car.update_position()
    car.draw()
    pygame.display.flip()
    clock.tick(speed)
