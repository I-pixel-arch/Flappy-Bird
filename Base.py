from Environment import *

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        # Move the base to left
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        # Move the base slide out of screen back right of the base of screen
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.WIDTH + self.x2
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.WIDTH + self.x1

    def draw(self, win):
        # Draw the bases
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))