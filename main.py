import pygame
import loop_control
from combat_scene import run
from menus import starting_menu
from menus import level_select_menu
pygame.init()

pygame.display.set_caption("Space Survival")

while loop_control.Master:
    if loop_control.Start_menu:
        starting_menu()
    elif loop_control.Level_select_menu:
        level_select_menu()
    else:
        run(loop_control.Level)

pygame.quit() 