import pygame
from bullets import standard_bullets
from bullets import swap_beam_tracker
from bullets import beam

pygame.init()

class ship:
    def __init__(self, player, speed, right, x, y, win, image, number):
        self.alliance = player
        self.right = right
        self.speed = speed
        self.image = image
        self.win = win
        if self.alliance == "player":
            self.swap = swap_beam_tracker(self.win)
        self.number = number
        self.clock = 0
        self.build_ship()
        self.ship_rect = self.ship_surface.get_rect(topleft = (x, y))

    def build_ship(self):
        if self.image == "standard":
            if self.alliance == "player":
                self.ship_surface = pygame.image.load('Assets/Ships/player_standard_ship.png').convert_alpha()
                self.bullets = standard_bullets(self.win, 8)
            else:
                if self.right:
                    self.ship_surface = pygame.image.load('Assets/Ships/red_standard_ship.png').convert_alpha()
                    self.bullets = standard_bullets(self.win, 8)
                else:
                    self.ship_surface = pygame.image.load('Assets/Ships/red_standard_ship_left.png').convert_alpha()
                    self.bullets = standard_bullets(self.win, -8)
            self.health = 3
            self.ammo = 10
        elif self.image == "lazer":
            if self.alliance == "player":
                self.ship_surface = pygame.image.load('Assets/Ships/player_lazer_ship.png').convert_alpha()
            else:
                if self.right:
                    self.ship_surface = pygame.image.load('Assets/Ships/red_lazer_ship.png').convert_alpha()
                else:
                    self.ship_surface = pygame.image.load('Assets/Ships/red_lazer_ship_left.png').convert_alpha()
            self.bullets = beam(self.win)
            self.health = 5
            self.ammo = 5
        elif self.image == "wave":
            if self.alliance == "player":
                self.ship_surface = pygame.image.load('Assets/Ships/player_wave_ship.png').convert_alpha()
            else:
                if self.right:
                    self.ship_surface = pygame.image.load('Assets/Ships/blue_wave_ship.png').convert_alpha()
                else:
                    self.ship_surface = pygame.image.load('Assets/Ships/blue_wave_ship_left.png').convert_alpha()
                
    def update_ship(self):
        self.win.blit(self.ship_surface, self.ship_rect)
        self.bullets.update_bullets()
        if self.alliance == "player":
            self.swap.update_bullets()
        self.clock += 1

    def moveright(self):
        if self.alliance == "player":
            if self.ship_rect.right < 900:
                self.ship_rect.right += self.speed
        else:
            self.ship_rect.right += self.speed

    def moveleft(self):
        if self.alliance == "player":
            if self.ship_rect.left > 0:
                self.ship_rect.left -= self.speed
        else:
            self.ship_rect.left -= self.speed

    def moveup(self):
        if self.alliance == "player":
            if self.ship_rect.top > 0:
                self.ship_rect.top -= self.speed
        else:
            self.ship_rect.top -= self.speed

    def movedown(self):
        if self.alliance == "player":
            if self.ship_rect.bottom < 500:
                self.ship_rect.bottom += self.speed
        else:
            self.ship_rect.bottom += self.speed

    def fire(self):
        if not self.alliance == "player" or self.ammo > 0:
            if self.right:
                self.bullets.fire(self.ship_rect.right, self.ship_rect.centery)
            else:
                self.bullets.fire(self.ship_rect.left, self.ship_rect.centery)
            self.ammo -= 1
        

    def swap_beam(self):
        self.swap.fire(self.ship_rect.left, self.ship_rect.centery)

    def bullets_array(self):
        return self.bullets.bullets_list
    
    def beam_array(self):
        return self.swap.bullets_list
    
    def enemy_hit(self, bullet):
        self.bullets.bullets_list.remove(bullet)   

    def beam_hit(self, beam):
        self.swap.bullets_list.remove(beam)     
