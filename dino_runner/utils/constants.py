import pygame
import os

pygame.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 22
FONT_STYLE = "freesansbold.ttf"
YELLOW = (255, 195, 0)
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUNDS_DIR = os.path.join(IMG_DIR, "Sounds")
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

theme_obj = "CACTUS"

#SOUNDS
#DINO
background_music = os.path.join(SOUNDS_DIR, "Dino/background.wav") 
sound_dead = os.path.join(SOUNDS_DIR, "Dino/sound_dead.wav")  
sound_gameover = os.path.join(SOUNDS_DIR, "Dino/sound_game-over.mp3")  
sound_jump = os.path.join(SOUNDS_DIR, "Dino/sound_jump.wav")  
sound_score = os.path.join(SOUNDS_DIR, "Dino/sound_score.wav")   

DINO_SOUNDS = {"background": background_music,
                "dead": sound_dead,
                "gameover": sound_gameover,
                "start": sound_score,
                "jump": sound_jump,
                "score": sound_score}

#MARIO
background_2 = os.path.join(SOUNDS_DIR, "Mario/musica_fundo.mp3") 
sound_dead = os.path.join(SOUNDS_DIR, "Dino/sound_dead.wav")  
sound_gameover = os.path.join(SOUNDS_DIR, "Dino/sound_game-over.mp3")  
sound_jump = os.path.join(SOUNDS_DIR, "Mario/mario_jump.wav")  
sound_score = os.path.join(SOUNDS_DIR, "Dino/sound_score.wav")   
sound_start = os.path.join(SOUNDS_DIR, "Mario/sound_start.wav")

MARIO_SOUNDS = {"background": background_2,
                "dead": sound_dead,
                "gameover": sound_gameover,
                "jump": sound_jump,
                "score": sound_score,
                "start": sound_start}



# Assets Constants
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
MARIO_MENU = pygame.image.load(os.path.join(IMG_DIR, "Other/Mario_menu.png"))
SONIC_MENU = pygame.image.load(os.path.join(IMG_DIR, "Other/Sonic_menu.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

dino_sprites = {DEFAULT_TYPE:{"run": RUNNING, "jump": JUMPING, "duck": DUCKING},
                 SHIELD_TYPE:{"run": RUNNING_SHIELD, "jump": JUMPING_SHIELD, "duck": DUCKING_SHIELD},
                 HAMMER_TYPE:{"run": RUNNING_HAMMER, "jump": JUMPING_HAMMER, "duck": DUCKING_HAMMER},} 

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png"))
]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

#MARIO
MARIO_SPRITE_SHEET = pygame.image.load(os.path.join(IMG_DIR, 'Mario/Mario_Sheet.png'))

#DEFAULT MARIO
MARIO_RUNNING = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 0), (32, 32))
    MARIO_RUNNING.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 0), (32, 32))
MARIO_JUMPING = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 0), (32, 32))
MARIO_DUCKING = pygame.transform.scale(img, (88, 94))

#SHIELD MARIO
MARIO_RUNNING_SHIELD = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32), (32, 32))
    MARIO_RUNNING_SHIELD.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 32), (32, 32))
MARIO_JUMPING_SHIELD = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 32), (32, 32))
MARIO_DUCKING_SHIELD = pygame.transform.scale(img, (88, 94))

#HAMMER MARIO
MARIO_RUNNING_HAMMER = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 2), (32, 32))
    MARIO_RUNNING_HAMMER.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 32 * 2), (32, 32))
MARIO_JUMPING_HAMMER = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 32 * 2), (32, 32))
MARIO_DUCKING_HAMMER = pygame.transform.scale(img, (88, 94))

#ALL MARIO
mario_sprites = {DEFAULT_TYPE:{"run": MARIO_RUNNING, "jump": MARIO_JUMPING, "duck": MARIO_DUCKING},
                 SHIELD_TYPE:{"run": MARIO_RUNNING_SHIELD, "jump": MARIO_JUMPING_SHIELD, "duck": MARIO_DUCKING_SHIELD},
                 HAMMER_TYPE:{"run": MARIO_RUNNING_HAMMER, "jump": MARIO_JUMPING_HAMMER, "duck": MARIO_DUCKING_HAMMER},} 

#MARIO ENEMIES
img = MARIO_SPRITE_SHEET.subsurface((32 * 0, 32 * 3), (32, 32))
ENEMY_5_BIRD = pygame.transform.scale(img, (88, 94))

ENEMY_1 = []
for i in range(1, 3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 3), (32, 32))
    ENEMY_1.append(pygame.transform.scale(img, (100, 114)))

ENEMY_2 = []
for i in range(3, 5):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 3), (32, 32))
    ENEMY_2.append(pygame.transform.scale(img, (100, 114)))

ENEMY_3 = []
for i in range(2):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 4), (32, 32))
    ENEMY_3.append(pygame.transform.scale(img, (88, 94)))

ENEMY_4_BIRD = []
for i in range(2, 5):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 4), (32, 32))
    ENEMY_4_BIRD.append(pygame.transform.scale(img, (88, 94)))
