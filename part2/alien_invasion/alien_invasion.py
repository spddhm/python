import pygame
from part2.alien_invasion.settings import Settings
from part2.alien_invasion.ship import Ship
import part2.alien_invasion.game_functions as gf
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings();
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dong")

    # 设置背景色
    # bg_color = ai_settings.bg_color

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
run_game()
