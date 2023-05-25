import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, ENEMY_1, ENEMY_2, ENEMY_3
from dino_runner.components.obstacles.obstacle import Obstacle

theme_obj = "CACTUS"

def change_theme_cactus(theme):
    global theme_obj
    if theme.lower() == "dino":
        theme_obj = "CACTUS"
    elif theme.lower() == "mario":
        theme_obj = "MARIO_ENEMYS"
    elif theme.lower() == "sonic":
        theme_obj = "SONIC_ENEMYS"

class Cactus(Obstacle):

    THEME = {
    "CACTUS": [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325),
    ],

    "MARIO_ENEMYS": [
        (ENEMY_1, 300),
        (ENEMY_2, 300),
        (ENEMY_3, 300)
    ],

    "SONIC_ENEMYS": [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325)
    ]
    }

    def __init__(self):
        self.theme = theme_obj
        self.list_image = self.THEME[self.theme]
        if self.theme == "CACTUS":
            self.type = random.randint(0, 2)
            image, cactus_pos = self.list_image[random.randint(0, len(self.list_image) - 1)]
            super().__init__(image, self.type)
            self.rect.y = cactus_pos
        else:
            self.type = 0
            super().__init__(self.list_image[random.randint(0, len(self.list_image) - 1)], "animation")
        