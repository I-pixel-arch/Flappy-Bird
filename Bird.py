from Environment import *

class Bird:
    # Bird images (different states)
    IMGS = BIRD_IMGS
    # Max rotation of the bird while jumping
    MAX_ROTATION = 25
    # Rotation of bird per tick
    ROTATION_VEL = 20
    # Durationg of each state of bird
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        # Position of the bird
        self.x, self.y = x, y
        # Tilt of bird (for animation)
        self.tilt = 0
        # Tick count used as a variable for change in time
        self.tick_count = 0
        # Current Velocity of the bird
        self.vel = 0
        # Current Height of the bird
        self.height = y
        # Current image of bird (for animation) 
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        # Change is velocity due to jump
        self.vel = -10.5
        # Reset tick counter
        self.tick_count = 0
        # Change current height of the bird
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # Displacement due to velocity
        disp = self.vel * self.tick_count + 1.5 * (self.tick_count ** 2)
        # Limiting the disp
        if disp >= 16:
            disp = 16
        if disp < 0:
            disp -= 2
        # Change y position
        self.y += disp
        # Tilt
        if disp < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VEL
        
    def draw(self, win):
        # Using img_count to keep track of ticks in animation
        self.img_count += 1
        # Setting the current image according to img_count and animation time
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        else:
            self.img = self.IMGS[0]
            self.img_count = 0
        
        # Diving state of bird
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # Rotating the bird image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft= (self.x, self.y)).center)
        # Render the bird
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self): 
        # Masks the pixels of the bird (used for collision detection)
        return pygame.mask.from_surface(self.img)