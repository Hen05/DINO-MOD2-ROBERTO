from dino_runner.utils.constants import BIRD, ENEMY_4_BIRD, ENEMY_5_BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
import random

theme_obj = "DINO_ENEMYS"

def change_theme_bird(theme):
    global theme_obj
    if theme.lower() == "dino":
        theme_obj = "DINO_ENEMYS"
    elif theme.lower() == "mario":
        theme_obj = "MARIO_ENEMYS"
    elif theme.lower() == "sonic":
        theme_obj = "SONIC_ENEMYS"

class Bird(Obstacle):
    
    THEME = {
    "DINO_ENEMYS": [
        (BIRD, 260)
    ],

    "MARIO_ENEMYS": [
        (ENEMY_4_BIRD, 245),
        (ENEMY_5_BIRD, 245)
    ],

    "SONIC_ENEMYS": [
        (BIRD, 260)
    ]
    }

    def __init__(self):
        self.theme = theme_obj
        self.list_image = self.THEME[self.theme]
        if self.theme == "BIRD_ENEMY":
            super().__init__(self.list_image[0], "animation")
        else:
            self.type = random.randint(0, len(self.list_image) - 1)
            if self.type == 1:
                super().__init__(self.list_image[self.type][0], -1)
                self.rect.y = self.list_image[self.type][1]
            else:
                super().__init__(self.list_image[self.type], "animation")

    # def draw(self, screen):
    #     screen.blit(self.image[self.step_index // 5], self.rect)
    #     self.step_index += 1

    #     if self.step_index >= 10:
    #         self.step_index = 0