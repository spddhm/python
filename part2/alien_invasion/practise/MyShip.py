import pygame

class MyShip():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('../images/ship.bmp');
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def updateShipLocation(self):
        if self.moving_right==True and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.ai_settings.move_location
        if self.moving_left==True and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.move_location


