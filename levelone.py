import pygame
import combat_scene
import loop_control
import all_dialogue
from background import main_window
from dialogue_box import dialogue

pygame.init()
pygame.font.init()

Background = main_window()
title = pygame.font.SysFont("monospace", 25)
subtitle = pygame.font.SysFont("monospace", 20)
clock = pygame.time.Clock()
enemy_number = 1
wave_complete_timer = 0

def levelone(time, wave):
    opening_scene()
    if wave == 1:
        if waveone(time):
            loop_control.Wave_complete = True
            wave = 2
    if wave == 2:
        if wavetwo(time):
            wave = 3

def opening_scene():

    text_tracker = 0
    opening_dialogue = dialogue(Background.win)
    opening_dialogue.display(all_dialogue.level_one[0][0])
    while loop_control.Story_scene:

        Background.draw_background()
        opening_dialogue.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop_control.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if text_tracker < 6:
                            text_tracker += 1
                            opening_dialogue.display(all_dialogue.level_one[0][text_tracker])
                        else:
                            loop_control.Story_scene = False
                            loop_control.Combat_scene = True
        pygame.display.update()

def waveone(time):
    global enemy_number
    global wave_complete_timer

    titlebox = title.render("Level One", 1, (255, 255, 255))
    subtitlebox = subtitle.render("Wave One", 1, (255, 255, 255))

    if loop_control.Wave_complete:
        Background.win.blit(titlebox, (350, 150))
    
    if time < 100:
        Background.win.blit(titlebox, (350, 150))
        Background.win.blit(subtitlebox, (375, 175))
    elif time == 100 or time == 200 or time == 300:
        #enemies 1-3
        combat_scene.spawn_enemy("red", 2, False, 900, 250, "standard", enemy_number)
        enemy_number += 1
    elif time == 500 or time == 600:
        #enemies 4-7
        combat_scene.spawn_enemy("red", 2, False, 900, 10, "standard", enemy_number)
        combat_scene.spawn_enemy("red", 2, False, 900, 450, "standard", enemy_number + 1)
        enemy_number += 2
    elif time == 900 or time == 1000:
        #enemies 8-11
        combat_scene.spawn_enemy("red", 2, False, 900, 10, "standard", enemy_number)
        combat_scene.spawn_enemy("red", 2, False, 900, 450, "standard", enemy_number + 1)
        enemy_number += 2
    elif time == 1200:
        #enemy 12
        combat_scene.spawn_enemy("red", 2, False, 900, 250, "lazer", enemy_number)
        enemy_number += 1
    elif time == 1500 or time == 1550 or time == 1600:
        #enemies 13-15
        combat_scene.spawn_enemy("red", 2, False, 900, 250, "standard", enemy_number)
        enemy_number += 1
    elif time == 1700 or time == 1750 or time == 1800:
        #enemies 16-18
        combat_scene.spawn_enemy("red", 2, False, 900, 175, "standard", enemy_number)
        enemy_number += 1
    elif loop_control.Wave_complete:
        Background.win.blit(titlebox, (350, 150))

    for enemy in combat_scene.enemies:
        enemy.moveleft()
        if enemy.ship_rect.x <= 0:
            combat_scene.despawn_enemy(enemy.number)

        if enemy.number == 8 or enemy.number == 10:
            if enemy.ship_rect.centery < 460:
                enemy.movedown()
        elif enemy.number == 9 or enemy.number == 11:
            if enemy.ship_rect.centery > 20:
                enemy.moveup()

        if enemy.clock == 134:
            enemy.fire()
            enemy.clock = 0
        
    if enemy_number == 18 and time > 1800:
        titlebox = title.render("Wave Complete", 1, (255, 255, 255))
        loop_control.Wave_complete = True
        wave_complete_timer = time

    if loop_control.Wave_complete and time >= wave_complete_timer + 100:
        return True
    else:
        return False

def wavetwo(time):
    global enemy_number

    titlebox = title.render("Level One", 1, (255, 255, 255))
    subtitlebox = subtitle.render("Wave Two", 1, (255, 255, 255))

    clock.tick(60)