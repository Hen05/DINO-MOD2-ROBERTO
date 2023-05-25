import pygame
from dino_runner.utils.constants import MARIO_SOUNDS, DINO_SOUNDS

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.music.load(DINO_SOUNDS["background"])

    def play_background_sound(self, theme):
        pygame.mixer.music.stop()
        if theme == "dino":
            self.music = pygame.mixer.music.load(DINO_SOUNDS["background"])
            pygame.mixer.music.set_volume(0.01)
        else:
            self.music = pygame.mixer.music.load(MARIO_SOUNDS["background"])
            pygame.mixer.music.set_volume(0.1)

        pygame.mixer.music.play(-1)
        

    def play_sound(self, type, theme):
        if theme == "dino":
            sound = pygame.mixer.Sound(DINO_SOUNDS[type.lower()])
            sound.set_volume(0.2)
            sound.play()
        else:
            sound = pygame.mixer.Sound(MARIO_SOUNDS[type.lower()])
            sound.set_volume(0.2)
            sound.play()
