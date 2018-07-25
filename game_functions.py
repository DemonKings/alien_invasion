import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """发射子弹的方法"""
    # 创建一颗子弹，添加到编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """键盘松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        # 如果是退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 如果是按下键盘
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        # 如果是松开键盘
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """重新绘制屏幕"""
    screen.fill(ai_settings.bg_color)
    # 画子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 画飞船
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    # 调用子弹移动的方法
    bullets.update()

    # 删除飞出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

