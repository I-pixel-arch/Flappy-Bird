from Bird import Bird
from Pipe import Pipe
from Base import Base
from Background import Background
from Environment import *

# Method to draw all objects to the window
def draw_window(objects):
    bird, base, pipes, bg, win, score = objects
    bg.draw(win)
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    text = STATS_FONT.render(f"Score : {score}", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    pygame.display.update()

def main():
    # Initialize the objects
    bird = Bird(230, 350)
    bg = Background()
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    objects = [bird, base, pipes, bg, win, score]

    # Game variables
    add_pipe = False
    running = True

    # Game loop
    while running:
        # Game FPS
        clock.tick(30)

        # Close game if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Pipe movements 
        passed_pipes = []
        for pipe in pipes:
            # Check collision
            if pipe.collide(bird):
                pass

            # Check if pipe has gone out of the window
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                passed_pipes.append(pipe)

            # Check if the pipe has passed the bird to initiate new pipe creation
            if not pipe.passed and pipe.x < bird.x : 
                pipe.passed = True
                add_pipe = True
            
            # Move Pipes
            pipe.move()

        # Adding new pipe 
        if  add_pipe:
            pipes.append(Pipe(700))
            objects[5] += 1
            add_pipe = False
        
        # Removing the pipes that have gone out of screen
        for pipe in passed_pipes:
            pipes.remove(pipe)

        # Moving the objects
        base.move()
        bg.move()
        #bird.move()
        
        # Check if bird has hit the ground
        if bird.y + bird.img.get_height() >= 730:
            pass
        
        # Draw the objects
        draw_window(objects)
    pygame.quit()
    quit()

main()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(main, 50)
    

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforwawrd.txt')
    run(config_path)