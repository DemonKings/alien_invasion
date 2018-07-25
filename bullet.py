import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()

        # 在（0,0）创建一个矩形再调整位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.screen = screen

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # 用小数表示子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """子弹移动的方法"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """画子弹的方法"""
        pygame.draw.rect(self.screen, self.color, self.rect)
