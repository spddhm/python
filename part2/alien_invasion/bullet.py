import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """ 在飞船所处的位置创建一个子弹对象 """
        super(Bullet, self).__init__()
        self.screen = screen

        # 在 (0,0) 处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx

