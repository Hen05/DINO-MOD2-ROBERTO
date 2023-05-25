import pygame
from random import randint
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(800, 1000)
        self.rect.y = randint(125, 175)
        self.start_time = 0
        self.duration = randint(5, 10)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)