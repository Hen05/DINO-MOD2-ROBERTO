import pygame
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH
from dino_runner.components.powerups.power_up import PowerUp
from pygame.sprite import Sprite

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

class HammerManager:
    def __init__(self):
        self.hammers = []

    def generate_hammer(self, x, y):
        if len(self.hammers) == 0:
            self.hammers.append(ThrowHammer(x, y))
            return True
        return False
    
    def update(self, game_speed, obstacles):
        for hammer in self.hammers:
            return hammer.update(game_speed, self.hammers, obstacles)

    def reset_hammers(self):
        self.hammers = []

    def draw(self, screen):
        for hammer in self.hammers:
            hammer.draw(screen)

class ThrowHammer(Sprite):
    def __init__(self, x, y):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, game_speed, hammers, obstacles):
        self.rect.x += game_speed
        for obstacle in obstacles:
            for hammer in hammers:
                if pygame.sprite.collide_mask(obstacle, hammer):
                    obstacles.remove(obstacle)
                    hammers.remove(hammer)
                    return False
        
        if self.rect.x > SCREEN_WIDTH:
            hammers.pop()
            return False
        
        return True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
       