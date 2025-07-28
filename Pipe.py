from Environment import *

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        # Defining position of the pipe
        self.x = x 
        self.height = 0
        self.top = 0
        self.bottom = 0
        # Image of top and bottom pipes
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG
        # Stores if the bird has already passed the pipes
        self.passed = False
        # Method to set random height of the pipes
        self.set_height()

    def set_height(self):
        # Change to random height of the pipe
        self.height = random.randrange(50, 450)
        # Position of top pipe
        self.top = self.height - self.PIPE_TOP.get_height()
        # Position of bottom pipe
        self.bottom = self.height + self.GAP

    def move(self):
        # Moving the pipe to the left
        self.x -= self.VEL

    def draw(self, win):
        # Draw both of the pipes
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        # Masking the pixels of the bird, top_pipe and bottom_pipe
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        # Check offset between bird and pipe
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        # Check if the is point of overlap with bottom of top pipe (gets 'None' if no overlap occurs)
        bottom_point = bird_mask.overlap(bottom_mask, bottom_offset)
        top_point = bird_mask.overlap(top_mask, top_offset)
        # Return if collision occurs
        if top_point or bottom_point: 
            return True
        return False