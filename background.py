import pygame

class main_window:
    def __init__(self):
        self.win = pygame.display.set_mode((900, 500))
        self.game_over = pygame.image.load('Assets/Backgrounds/Game_Over.png').convert_alpha()

    def draw_background(self):
        self.win.fill('black')

    def draw_gameover(self):
        self.win.blit(self.game_over, (0,0))
