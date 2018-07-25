import pygame


class Ship:
    """飞船类"""
    def __init__(self, screen, ai_settings):
        # 指明飞船描绘的地方
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船的图像
        self.image = pygame.image.load('images/ship.bmp')
        # 图像的外接矩形
        self.rect = self.image.get_rect()
        # 屏幕的外接矩形
        self.screen_rect = self.screen.get_rect()

        # 将飞船位置设置在屏幕下方中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # centerx只能存储整数，创建center属性存储小数
        self.center = float(self.rect.centerx)

        # 控制飞船移动的标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置画飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志控制飞船移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据center属性的值，更新rect的centerx
        self.rect.centerx = self.center
