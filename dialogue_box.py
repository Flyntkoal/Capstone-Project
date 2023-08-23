import pygame
import time

pygame.init()
pygame.font.init()

class dialogue:
    def __init__(self, win):
        self.win = win
        self.dialogue = pygame.font.SysFont("monospace", 15)
        self.message = "Empty Message"
        self.message_spacer = 0
        self.clock = 0

    def display(self, message):
        self.message = message
        self.message_spacer = 0

    def update(self):
        if self.message_spacer < len(self.message):
            dialoguebox = self.dialogue.render(self.message[0:self.message_spacer], 1, (255,255,255))
            self.win.blit(dialoguebox, (75,325))
            self.clock += 1
            if self.clock == 20:
                self.message_spacer += 1
                self.clock = 0
        else:
            dialoguebox = self.dialogue.render(self.message, 1, (255,255,255))
            self.win.blit(dialoguebox, (75,325))
