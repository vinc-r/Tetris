import pygame
from constants import CUBE_SIZE


class Cube(pygame.sprite.Sprite):

    def __init__(self, x, y, type="bg", pos=None):
        super().__init__()
        self.image = pygame.image.load('img/cube/'+type+'.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # position of cube in tetrimono (in order to spin later)
        # stay None for wall cubes, empty cubes ans O cubes
        self.pos = pos

    def move_down(self):
        self.rect.y += CUBE_SIZE

    def move_right(self):
        self.rect.x += CUBE_SIZE

    def move_left(self):
        self.rect.x -= CUBE_SIZE

    def move_honrizontal(self, mvt_pixels):
        self.rect.x += mvt_pixels
