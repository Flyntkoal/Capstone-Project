import combat_scene
import random

cur_player_ship = 0

def demo(multi_spawn):
    if random.randint(0, 100) == 0:
        rand_ship_generator(multi_spawn)
    for enemy in combat_scene.enemies:
        if enemy.right:
            enemy.moveright()
        else:
            enemy.moveleft()
        
        if enemy.clock == enemy.countdown:
                enemy.fire()
                enemy.clock = 0


def rand_ship_generator(multi_spawn):
    #random spawn point
    rand_x = random.randint(0,1)
    rand_y = random.randint(0, 500)

    if rand_x == 0:
        rand_right = True
    else:
        rand_right = False
        rand_x = 900

    #random speed
    rand_speed = random.randint(1,5)

    #random ship type
    rand_type = "standard"

    if multi_spawn:
        ship_type_num = random.randint(1,7)
    else:
        ship_type_num = 1

    if ship_type_num == 2:
        rand_type = "lazer"
    elif ship_type_num == 3:
        rand_type = "exhaust"
    elif ship_type_num == 4:
        rand_type = "shield"
    elif ship_type_num == 5:
        rand_type = "rapidfire"
    elif ship_type_num == 6:
        rand_type = "wave"
    elif ship_type_num == 7:
        rand_type = "scatter"
    
    if rand_type == "wave" or rand_type == "scatter":
        rand_alliance = "blue"
    else:
        rand_alliance = "red"

    combat_scene.spawn_enemy(rand_alliance, rand_speed, rand_right, rand_x, rand_y, rand_type, 0)

