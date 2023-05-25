import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import mario_sprites, RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, HAMMER_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER
from dino_runner.components.powerups.hammer import HammerManager

duck_img = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
jump_img = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
run_img = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

X_POS = 80
Y_POS = 310
y_pos_duck = 340
JUMP_VEL = 8.5

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = run_img[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = Y_POS
        self.mask = pygame.mask.from_surface(self.image)
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.hammer_manager = HammerManager()
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.show_text = False
        self.has_hammer = False
        self.shield_time_up = 0
        
    def change_theme(self, theme):
        global duck_img, jump_img, run_img, y_pos_duck
        if theme == "mario":
            duck_img = { DEFAULT_TYPE: mario_sprites[DEFAULT_TYPE]["duck"], SHIELD_TYPE: mario_sprites[SHIELD_TYPE]["duck"], HAMMER_TYPE: mario_sprites[HAMMER_TYPE]["duck"]}
            jump_img = { DEFAULT_TYPE: mario_sprites[DEFAULT_TYPE]["jump"], SHIELD_TYPE: mario_sprites[SHIELD_TYPE]["jump"], HAMMER_TYPE: mario_sprites[HAMMER_TYPE]["jump"]}
            run_img = { DEFAULT_TYPE: mario_sprites[DEFAULT_TYPE]["run"], SHIELD_TYPE: mario_sprites[SHIELD_TYPE]["run"], HAMMER_TYPE: mario_sprites[HAMMER_TYPE]["run"]}
            y_pos_duck = 320
            self.mask = pygame.mask.from_surface(self.image)
        elif theme == "sonic":
            duck_img = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
            jump_img = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
            run_img = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
            y_pos_duck = 340
            self.mask = pygame.mask.from_surface(self.image)
        elif theme == "dino":
            duck_img = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
            jump_img = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
            run_img = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
            y_pos_duck = 340
            self.mask = pygame.mask.from_surface(self.image)

    def update(self, user_input, game_speed, obstacles, music, theme):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump(music, theme)
        elif self.dino_duck:
            self.duck()

        if self.has_hammer:
            self.has_hammer = self.hammer_manager.update(game_speed, obstacles)
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        
        if user_input[pygame.K_SPACE] and not self.has_hammer and self.hammer:
            self.has_hammer = self.hammer_manager.generate_hammer(self.rect.x, self.rect.y)


        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = run_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = Y_POS
        self.step_index += 1
        self.mask = pygame.mask.from_surface(self.image)
    
    def jump(self, music, theme):
        self.image = jump_img[self.type]
        if self.jump_vel == JUMP_VEL:
            music.play_sound("jump", theme)
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -JUMP_VEL:
            self.rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
        self.mask = pygame.mask.from_surface(self.image)

    def duck(self):
        if type(duck_img[self.type]) == list:
            self.image = duck_img[self.type][self.step_index // 8]
        else:
            self.image = duck_img[self.type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = y_pos_duck
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.has_hammer:
            self.hammer_manager.draw(screen)