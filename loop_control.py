Master = True
Start_menu = True
Level_select_menu = False
Pause_menu = False
In_game = True
Story_scene = True
Combat_scene = True
Game_over = False

Level = 1

def quit():
    global Master
    global Start_menu
    global Level_select_menu
    global Pause_menu
    global In_game
    global Story_scene
    global Combat_scene
    global Game_over
    global Level

    Master = False
    Start_menu = False
    Level_select_menu = False
    Pause_menu = False
    In_game = False
    Story_scene = False
    Combat_scene = False
    Game_over = False
    Level = 1
