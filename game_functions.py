import sys
import pygame

from alien import Alien
from bullet import Bullet


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """重新绘制屏幕"""
    screen.fill(ai_settings.bg_color)
    # 画子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 画飞船
    ship.blitme()
    # 画外星人
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets, aliens, ai_settings, screen, ship):
    # 调用子弹移动的方法
    bullets.update()

    # 删除飞出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 如果子弹击中外星人，则删除子弹和外星人
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 如果没有外星人，则创建
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


def change_fleet_direction(aliens, ai_settings):
    """将外星人向下移并改变方向"""
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edgs(aliens, ai_settings):
    """检测是否有外星人到达边缘"""
    for alien in aliens.sprites():
        if alien.check_edgs():
            change_fleet_direction(aliens, ai_settings)
            break


def update_aliens(aliens, ai_settings):
    check_fleet_edgs(aliens, ai_settings)
    # 调用外星人移动的方法
    aliens.update()


def get_number_aliens_x(ai_settings, screen):
    """计算每行容纳多少外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, screen, ship):
    """计算容纳多少行外星人"""
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, alien_number, row_number, aliens):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    number_alien_x = get_number_aliens_x(ai_settings, screen)
    number_rows = get_number_rows(ai_settings, screen, ship)

    # 添加外星人到编组中
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, alien_number, row_number, aliens)

