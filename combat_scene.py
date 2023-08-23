import pygame
import loop_control
from background import main_window
from ships import ship
from levelone import levelone
from controls import control
from menus import pause_menu

pygame.init()
pygame.font.init()

Background = main_window()
Starting_ship = ship("player", 3, True, 450, 250, Background.win, "wave", 0)
Player = Starting_ship
clock = pygame.time.Clock()
enemies = []
enemy_count = 0
time = 0
health = pygame.font.SysFont("monospace", 20)

def Check_Collision():
    global enemy_count
    for i in enemies:
        if Player.bullets.check_collision(i):
            if i in enemies:
                enemies.remove(i)
                enemy_count -= 1
        
        if Player.swap.check_collision(i):
            Swap_ships(Player, i)

        if i.bullets.check_collision(Player):
            if Player.health > 0:
                Player.health -= 1
                #Player.health += 1
            else:
                return True
    return False
    
def Swap_ships(player_ship, enemy_ship):
    Temp_shiprect = player_ship.ship_rect
    Temp_image = player_ship.image

    player_ship.ship_rect = enemy_ship.ship_rect
    player_ship.image = enemy_ship.image
    player_ship.build_ship()

    enemy_ship.ship_rect = Temp_shiprect
    enemy_ship.image = Temp_image
    enemy_ship.build_ship()

def run(level):
    cur_level = level
    cur_wave = 1
    game_over_switch = False
    global time
    global Player
    time = 0
    while loop_control.In_game:
        clock.tick(60)
        if loop_control.Combat_scene:
            Background.draw_background()
            healthbox = health.render("Health: " + str(Player.health), 1, (255, 255, 255))
            ammobox = health.render("Ammo: " + str(Player.ammo), 1, (255, 255, 255))
            if cur_level == 1:
                if levelone(time, cur_wave):
                    time = 0
                    cur_wave += 1
                    if cur_wave == 5:
                        cur_wave = 0
                        cur_level = 2
            
            if Check_Collision():
                game_over_switch = True
            else:
                time = time + 1

            control(Player)
            Player.update_ship()
            for enemy in enemies:
                enemy.update_ship()
            Background.win.blit(healthbox, (0, 0))
            Background.win.blit(ammobox, (0, 15))
            pygame.display.update()

            if game_over_switch:
                loop_control.Combat_scene = False
                loop_control.Game_over = True
                reset_game()
                time = 0
                game_over_switch = False
        
        elif loop_control.Game_over:
            Background.draw_background()
            Background.draw_gameover()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop_control.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        loop_control.Game_over = False
                        loop_control.Combat_scene = True
        elif loop_control.Pause_menu:
            pause_menu()

def ship_test():
    while loop_control.In_game:
        clock.tick(60)
        Background.draw_background()
        Player.ammo = 10
        control(Player)
        Player.update_ship()
        pygame.display.update()

def wave_complete():
    Background.draw_background()

def spawn_enemy(alliance, speed, right, x, y, image, number):
    global enemy_count
    enemies.append(ship(alliance, speed, right, x, y, Background.win, image, number))
    enemy_count += 1

def despawn_enemy(num):
    global enemy_count
    for enemy in enemies:
        if enemy.number == num:
            enemies.remove(enemy)
            enemy_count -= 1

def reset_game():
    global time
    clear_enemies()
    clear_bullets()
    Player.build_ship()
    Player.ship_rect.x = 450
    Player.ship_rect.y = 250
    time = 0

def clear_enemies():
    global enemy_count
    enemies.clear()
    enemy_count = 0

def clear_bullets():
    Player.bullets_array().clear()
    Player.beam_array().clear()