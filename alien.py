
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外形人类"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人的图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 小数存储外星人的位置
        self.x = float(self.rect.x)

    def blitme(self):
        """画外星人的方法"""
        self.screen: pygame.Surface
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向左或者向右外星人移动"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edgs(self):
        """如果外星人位于边缘返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
