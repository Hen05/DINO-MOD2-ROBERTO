import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus, change_theme_cactus
from dino_runner.components.obstacles.bird import Bird, change_theme_bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird()
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if pygame.sprite.collide_mask(game.player, obstacle):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.all_time_score += game.score + 1
                    game.update_score_rank()
                    break
                else:
                    self.obstacles.remove(obstacle)
    
    def reset_obstacles(self):
        self.obstacles = []

    def change_theme(self, theme):
        change_theme_cactus(theme)
        change_theme_bird(theme)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)