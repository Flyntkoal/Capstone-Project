import pygame

class bullet:
    def __init__(self, win, color, speed, x, y):
        self.win = win
        self.bullets_surface = pygame.Surface((5,5))
        self.bullets_surface.fill(color)
        self.bullets_rect = self.bullets_surface.get_rect(topleft=(x,y))
        self.speed = speed
        self.win.blit(self.bullets_surface, (self.bullets_rect.x, self.bullets_rect.y))

    def move_horz(self):
        self.bullets_rect.x += self.speed

    def move_vert(self):
        self.bullets_rect.y += self.speed

    def draw(self):
        self.win.blit(self.bullets_surface, (self.bullets_rect.x, self.bullets_rect.y))

    def x_value(self):
        return self.bullets_rect.x
    
    def y_value(self):
        return self.bullets_rect.y
    
class swap_beam:
    def __init__(self, win, x, y):
        self.bullet_list = []
        self.firing = True
        self.win = win
        self.starting_x = x
        self.starting_y = y
    
    def update_beam(self):
        if self.firing:
            if len(self.bullet_list) < 25:
                self.bullet_list.append(bullet(self.win, 'Red', 10, self.starting_x, self.starting_y))
            else:
                self.firing = False
        
        for b in self.bullet_list:
            if b.bullets_rect.x > self.starting_x + 350:
                b.bullets_rect.y += 5
                b.speed = b.speed * -1
            
            b.move_horz()

            if b.bullets_rect.x < self.starting_x:
                self.bullet_list.remove(b)
            
            b.draw()

class swap_beam_tracker:
    def __init__(self, win):
        self.win = win
        self.bullets_list = []
        self.firing = False

    def update_bullets(self):
        for cur_beam in self.bullets_list:
            cur_beam.update_beam()
            if len(cur_beam.bullet_list) == 0:
                self.bullets_list.remove(cur_beam)

    def fire(self, x, y):
        self.bullets_list.append(swap_beam(self.win, x, y))

class standard_bullets:
    def __init__(self, win, speed):
        self.bullets_list = []
        self.win = win
        self.speed = speed

    def update_bullets(self):
        for b in self.bullets_list:
            b.move_horz()
            b.draw()
            if b.x_value() <= 0 or b.x_value() >= 900:
                self.bullets_list.remove(b)

    def fire(self, x, y):
        self.bullets_list.append(bullet(self.win, 'White', self.speed, x, y))

class beam:
    def __init__(self, win):
        self.win = win
        self.bullets_list = []
        self.x_right = 0
        self.x_left = 0
        self.y_start = 0
        self.beam_countdown = 10
    
    def update_bullets(self):
        if len(self.bullets_list) > 0:
            if self.beam_countdown > 0:
                self.beam_countdown -= 1
            elif self.beam_countdown == 0:
                while self.x_left > 0 or self.x_right < 900:
                    self.bullets_list.append(bullet(self.win, 'White', 0, self.x_left, self.y_start))
                    self.bullets_list.append(bullet(self.win, 'White', 0, self.x_right, self.y_start))
                    self.x_left -= 1
                    self.x_right += 1
                self.beam_countdown -= 1
            elif self.beam_countdown > -50:
                self.beam_countdown -= 1
            else:
                self.bullets_list.clear()
                self.beam_countdown = 5
            for b in self.bullets_list:
                b.draw()

    
    def fire(self, x, y):
        self.bullets_list.append(bullet(self.win, 'White', 0, x, y + 30))
        self.x_right = x
        self.x_left = x
        self.y_start = y + 30

class wave_shot:
    def __init__(self, win):
        self.win = win
        self.bullets_list = []