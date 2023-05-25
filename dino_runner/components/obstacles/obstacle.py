import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, images, type):
        self.image = images
        self.type = type
        if self.type == "animation":
            self.image = images[0][0]
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH
            self.rect.y = images[1]
            self.mask = pygame.mask.from_surface(self.image)
            self.step_animation = 0
            self.list_images = images[0]
        elif self.type >= 0:
            self.rect = self.image[self.type].get_rect()
            self.rect.x = SCREEN_WIDTH
            self.mask = pygame.mask.from_surface(self.image[self.type])
        else:
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH
            self.mask = pygame.mask.from_surface(self.image)
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.type == "animation":
            self.step_animation += 1
            self.image = self.list_images[self.step_animation // 5]
            if self.step_animation >= 9:
                self.step_animation = 0
        if self.rect.x < - self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        if self.type == "animation" or self.type == -1:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image[self.type], (self.rect.x, self.rect.y))