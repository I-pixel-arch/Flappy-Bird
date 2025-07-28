from Environment import *

class Background:
    VEL = 5
    WIDTH = BG_IMG.get_width()
    IMG = BG_IMG

    def __init__(self):
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        # Move the background to left
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        # Move the background slide out of screen back right of the background of screen
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.WIDTH + self.x2
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.WIDTH + self.x1

    def draw(self, win):
        # Draw the backgrounds
        win.blit(self.IMG, (self.x1, 0))
        win.blit(self.IMG, (self.x2, 0))