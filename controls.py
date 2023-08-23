import pygame
import loop_control
pygame.init()

def control(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_control.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.fire()
            if event.key == pygame.K_x:
                player.swap_beam()
            if event.key == pygame.K_ESCAPE:
                loop_control.Combat_scene = False
                loop_control.Pause_menu = True
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.moveright()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.moveleft()

    if pygame.key.get_pressed()[pygame.K_UP]:
        player.moveup()

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player.movedown()