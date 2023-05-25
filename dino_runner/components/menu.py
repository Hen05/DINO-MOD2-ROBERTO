import pygame
from pygame.locals import *
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.utils.constants import YELLOW, JUMPING, SCREEN_HEIGHT, SCREEN_WIDTH, MARIO_RUNNING, SONIC_MENU, GAME_OVER
 
HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

DINO_IMG = JUMPING
SONIC_IMG = SONIC_MENU
MARIO_IMG = MARIO_RUNNING[0]


FONT_SIZE = 40

class Menu:
    def __init__(self):
        self.options = ["start", "shop", "exit"]
        self.menu_index = 0
        self.shop_index = 0
        self.shop_menu = False
        self.shop_options = [{"name": "Dino", "img": DINO_IMG, "price": 0, "purchased": True},
                             {"name": "Mario", "img": MARIO_IMG, "price": 10000, "purchased": False},
                             {"name": "Sonic", "img": SONIC_IMG, "price": "NEXT UPDATE", "purchased": False}]
        self.selected_theme = 0
        self.rank_menu = False
        self.menu_img = JUMPING

    def select(self, list, index):
        return list[index].lower()

    def change_selection(self, dir, index, list):
        index += dir
        if index >= len(list):
            index = 0
        elif index < 0:
            index = len(list) - 1
        return index

    def check_index(self, index_selected, index):
        if index_selected == index:
            return YELLOW
        else:
            return (0, 0, 0)

    def change_menu_img(self, theme):
        if theme == "dino":
            self.menu_img = JUMPING
        else:
            self.menu_img = MARIO_RUNNING[0]

    def game_quit(self, game):
        game.playing = False
        game.running = False

    def exec_esc(self, game):
        if self.shop_menu:
            self.shop_menu = False
        elif self.rank_menu:
            self.rank_menu = False
        else:
            self.game_quit(game)
    
    def show_menu(self, game, screen, score, death_count, all_time_score, rank_menu):
        if not self.shop_menu and not self.rank_menu:
            self.draw_menu(screen, score, death_count)
            self.handle_events_on_menu(game)
        elif self.shop_menu:
            self.draw_shop_menu(screen, all_time_score)
            self.handle_events_on_shop_menu(game)
        elif self.rank_menu:
            self.draw_rank_menu(screen, rank_menu)
            self.handle_events_on_rank_menu(game)

    def handle_events_on_rank_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exec_esc(game)
            if event.type == QUIT:
                game.playing = False
                game.running = False

    def handle_events_on_shop_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if [K_SPACE, K_KP_ENTER, K_RETURN].__contains__(event.key):
                    item = self.shop_options[self.shop_index]
                    if not item["purchased"] and self.shop_index != 2:
                        if game.all_time_score >= item["price"]:
                            game.all_time_score -= item["price"]
                            game.change_theme(item["name"].lower())
                            self.selected_theme = self.shop_index
                            item["purchased"] = True
                            game.music.play_background_sound(game.theme_obj)
                    elif item["purchased"]:
                        game.change_theme(item["name"].lower())
                        self.selected_theme = self.shop_index
                        game.music.play_background_sound(game.theme_obj)

                elif event.key == K_ESCAPE:
                    self.exec_esc(game)
                elif event.key == K_LEFT:
                    self.shop_index = self.change_selection(-1, self.shop_index, self.shop_options)
                elif event.key == K_RIGHT:
                    self.shop_index = self.change_selection(1, self.shop_index, self.shop_options)
            elif event.type == QUIT:
                game.playing = False
                game.running = False

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if [K_SPACE, K_KP_ENTER, K_RETURN].__contains__(event.key):
                    option_selected = self.select(self.options, self.menu_index)
                    if ["start", "restart"].__contains__(option_selected):
                        game.music.play_sound("start", game.theme_obj)
                        game.run()
                        game.music.play_sound("gameover", game.theme_obj)
                    elif option_selected == "shop":
                        self.shop_menu = True
                    elif option_selected == "exit":
                        self.game_quit(game)
                    elif option_selected == "rank":
                        self.rank_menu = True
                elif event.key == K_ESCAPE:
                    self.exec_esc(game)
                elif event.key == K_UP:
                    self.menu_index = self.change_selection(-1, self.menu_index, self.options)
                elif event.key == K_DOWN:
                    self.menu_index = self.change_selection(1, self.menu_index, self.options)
            elif event.type == QUIT:
                game.playing = False
                game.running = False

    def draw_shop_menu(self, screen, all_time_score):
        screen.fill((255, 255, 255))
        draw_message_component(
                f"Shop",
                screen,
                font_size = FONT_SIZE,
                pos_y_center = FONT_SIZE * 1.5
            )
        draw_message_component(
                f"Shop points: {all_time_score}",
                screen,
                pos_x_center = 900,
                pos_y_center = 50
            )

        x = (SCREEN_WIDTH // 3) / 2
        for index, option in enumerate(self.shop_options):
            x_option = x + ((SCREEN_WIDTH // 3 * index))
            color = self.check_index(self.shop_index, index)
            screen.blit(option["img"], (x_option - option["img"].get_width() // 2 + 5, HALF_SCREEN_HEIGHT - FONT_SIZE * 2))
            draw_message_component(
                f"{option['name']}",
                screen,
                font_color = color,
                pos_x_center = x_option,
                pos_y_center = HALF_SCREEN_HEIGHT + FONT_SIZE
            )
            if not option["purchased"]:
                draw_message_component(
                    f"{option['price']}",
                    screen,
                    font_color = color,
                    pos_x_center = x_option,
                    pos_y_center = HALF_SCREEN_HEIGHT + FONT_SIZE * 2
                )
            elif option["purchased"]:
                draw_message_component(
                    f"Purchased",
                    screen,
                    font_color = color,
                    pos_x_center = x_option,
                    pos_y_center = HALF_SCREEN_HEIGHT + FONT_SIZE * 2
                )
            if self.selected_theme == index:
                draw_message_component(
                    f"Selected",
                    screen,
                    pos_x_center = x_option,
                    pos_y_center = HALF_SCREEN_HEIGHT + FONT_SIZE * 3
                )

        pygame.display.flip()

    def draw_rank_menu(self, screen, rank_menu):
        screen.fill((255, 255, 255))
        height = screen.get_height()
        draw_message_component(
                "Rank",
                screen,
                font_size = FONT_SIZE, 
                pos_y_center = FONT_SIZE * 1.5
                )
        for index, option in enumerate(rank_menu):
            draw_message_component(
                f"{index + 1}. {option}",
                screen,
                font_size = FONT_SIZE,
                pos_y_center = FONT_SIZE + height / 4 + (FONT_SIZE * 2 * index)
            )
        pygame.display.flip()

    def draw_menu(self, screen, score, death_count):
        screen.fill((255, 255, 255))
        height = screen.get_height()
        if death_count == 0:
            self.options = ["start", "shop", "exit"]
        else: 
            self.options = ["restart", "shop", "rank", "exit"]
            draw_message_component(
                f"Last score: {score}",
                screen,
                pos_x_center = HALF_SCREEN_WIDTH - HALF_SCREEN_WIDTH / 2
            )
            draw_message_component(
                f"Death count: {death_count}",
                screen,
                pos_x_center = HALF_SCREEN_WIDTH + HALF_SCREEN_WIDTH / 2
            )
            screen.blit(GAME_OVER, (HALF_SCREEN_WIDTH - 190, HALF_SCREEN_HEIGHT - 280 ))

        menu_img_width = self.menu_img.get_width()
        menu_img_height = self.menu_img.get_height()
        scaled_mult = 2
        menu_img_scaled = pygame.transform.scale(self.menu_img, (menu_img_width * scaled_mult, menu_img_height * scaled_mult))
        screen.blit(menu_img_scaled, (10 + HALF_SCREEN_WIDTH - menu_img_scaled.get_width() / 2, HALF_SCREEN_HEIGHT - FONT_SIZE * 3.7 - self.menu_img.get_height()))

        for index, option in enumerate(self.options):
            draw_message_component(
                f"{option.capitalize()}",
                screen,
                font_color = self.check_index(self.menu_index, index),
                font_size = FONT_SIZE,
                pos_y_center = FONT_SIZE * 3 + height / 3 + (FONT_SIZE * 2 * index)
            )
        pygame.display.flip()
