import pygame
from random import randint
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def generate_power_up(self, score):
        power_up_types = [
            Shield(),
            Hammer()
        ]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += randint(200, 300)
            self.power_ups.append(power_up_types[randint(0, 1)])

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if pygame.sprite.collide_mask(player, power_up):
                    player.shield = False
                    player.hammer = False
                    power_up.start_time = pygame.time.get_ticks()
                    player.has_power_up = True
                    player.type = power_up.type
                    player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)    
                    if power_up.type == SHIELD_TYPE:
                        player.shield = True
                    else:
                        player.hammer = True

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)

    