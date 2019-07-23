import sys
import pygame
# from part2.alien_invasion.practise.MyShip import MyShip

def check_move_down(event, myShip, mySettings):
    if event.key == pygame.K_RIGHT:
        myShip.moving_right = True
    if event.key == pygame.K_LEFT:
        myShip.moving_left = True
def check_move_up(event, myShip, mySettings):
    if event.key == pygame.K_RIGHT:
        myShip.moving_right = False
    if event.key == pygame.K_LEFT:
        myShip.moving_left = False
def check_event(myShip, mySettings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_move_down(event, myShip, mySettings)
        if event.type == pygame.KEYUP:
            check_move_up(event, myShip, mySettings)
def set_backcolor(myShip, screen, mySettings):

    screen.fill(mySettings.bg_color)

    myShip.blitme()
    #  让最近绘制的屏幕可见
    pygame.display.flip()


