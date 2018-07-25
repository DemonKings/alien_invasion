class Settings:
    """存储相关设置的类"""
    def __init__(self):
        # 屏幕宽度
        self.screen_width = 1200
        # 屏幕高度
        self.screen_height = 600
        # 屏幕背景颜色
        self.bg_color = (230, 230, 230)
        # 飞机移动速度
        self.ship_speed_factor = 1.5
        # 子弹相关设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
