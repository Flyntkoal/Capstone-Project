import pygame
import loop_control
from ships import ship
from background import main_window

Background = main_window()
Cursor = ship(True, 3, True, 250, 200, Background.win, "standard", 0)
Cursor_place = 0

def starting_menu():
    global Cursor_place
    title = pygame.font.SysFont("monospace", 50)
    option = pygame.font.SysFont("monospace", 30)
    titlebox = title.render("Space Survival", 1, (255, 255, 255))
    newgamebox = option.render("New Game", 1, (255, 255, 255))
    selectlevelbox = option.render("Select Level", 1, (255, 255, 255))
    quitbox = option.render("Quit", 1, (255, 255, 255))
    Background.draw_background()
    Background.win.blit(titlebox, (210, 100))
    Background.win.blit(newgamebox, (300, 200))
    Background.win.blit(selectlevelbox, (300, 250))
    Background.win.blit(quitbox, (300, 300))
    if Cursor_place == 0:
        Cursor.ship_rect.y = 200
    elif Cursor_place == 1:
        Cursor.ship_rect.y = 250
    elif Cursor_place == 2:
        Cursor.ship_rect.y = 300
    Cursor.update_ship()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_control.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if Cursor_place == 0:
                    loop_control.Start_menu = False
                    loop_control.Combat_scene = True
                elif Cursor_place == 1:
                    loop_control.Start_menu = False
                    loop_control.Level_select_menu = True
                    Cursor_place = 0
                elif Cursor_place == 2:
                    loop_control.quit()
            if event.key == pygame.K_DOWN:
                Cursor_place += 1
                if Cursor_place > 2:
                    Cursor_place = 0
            if event.key == pygame.K_UP:
                Cursor_place -= 1
                if Cursor_place < 0:
                    Cursor_place = 2

def level_select_menu():
    global Cursor_place
    title = pygame.font.SysFont("monospace", 50)
    option = pygame.font.SysFont("monospace", 30)
    titlebox = title.render("Space Survival", 1, (255, 255, 255))
    levelonebox = option.render("Level One", 1, (255, 255, 255))
    backbox = option.render("Back", 1, (255, 255, 255))
    Background.draw_background()
    Background.win.blit(titlebox, (210, 100))
    Background.win.blit(levelonebox, (300, 200))
    Background.win.blit(backbox, (300, 250))
    if Cursor_place == 0:
        Cursor.ship_rect.y = 200
    elif Cursor_place == 1:
        Cursor.ship_rect.y = 250
    Cursor.update_ship()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_control.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if Cursor_place == 0:
                    loop_control.Level_select_menu = False
                    loop_control.Combat_scene = True
                elif Cursor_place == 1:
                    loop_control.Level_select_menu = False
                    loop_control.Start_menu = True
                    Cursor_place = 0
            if event.key == pygame.K_DOWN:
                Cursor_place += 1
                if Cursor_place > 1:
                    Cursor_place = 0
            if event.key == pygame.K_UP:
                Cursor_place -= 1
                if Cursor_place < 0:
                    Cursor_place = 1

def pause_menu():
    global Cursor_place
    pause = pygame.font.SysFont("monospace", 20)
    option = pygame.font.SysFont("monospace", 30)
    pausebox = pause.render("Pause", 1, (255, 255, 255))
    continuebox = option.render("Continue", 1, (255, 255, 255))
    quitbox = option.render("Quit", 1, (255, 255, 255))
    Background.draw_background()
    Background.win.blit(pausebox, (0, 0))
    Background.win.blit(continuebox, (300, 200))
    Background.win.blit(quitbox, (300, 250))
    if Cursor_place == 0:
        Cursor.ship_rect.y = 200
    elif Cursor_place == 1:
        Cursor.ship_rect.y = 250
    Cursor.update_ship()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_control.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if Cursor_place == 0:
                    loop_control.Pause_menu = False
                    loop_control.Combat_scene = True
                elif Cursor_place == 1:
                    loop_control.Pause_menu = False
                    loop_control.In_game = False
                    loop_control.Start_menu = True
                    Cursor_place = 0
            if event.key == pygame.K_DOWN:
                Cursor_place += 1
                if Cursor_place > 1:
                    Cursor_place = 0
            if event.key == pygame.K_UP:
                Cursor_place -= 1
                if Cursor_place < 0:
                    Cursor_place = 1


#def game_over_menu():