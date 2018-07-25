import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame，创建一个窗口
    pygame.init()
    # 创建Settings对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('alien_invasion')

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)

    # 创建一个存储子弹的编组
    bullets = Group()

    # 游戏的主循环
    while True:

        # 监视鼠标和键盘事件
        gf.check_events(ship, ai_settings, screen, bullets)
        # 调用飞船移动的方法
        ship.update()
        # 调用管理子弹的方法
        gf.update_bullet(bullets)
        # 每次循环重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()

