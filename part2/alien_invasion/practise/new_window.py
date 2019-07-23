import sys
import pygame
import part2.alien_invasion.practise.function as pf
from part2.alien_invasion.practise.MyShip import MyShip
from part2.alien_invasion.practise.MySettings import MySettings


def blue_window():
    pygame.init()
    mySettings = MySettings() # 实例化对象
    screen = pygame.display.set_mode((mySettings.screen_width, mySettings.screen_height));
    pygame.display.set_caption("dong")

    myShip = MyShip(mySettings, screen)

    while True:
        pf.check_event(myShip, mySettings)
        myShip.updateShipLocation()
        pf.set_backcolor(myShip, screen, mySettings)

blue_window();
