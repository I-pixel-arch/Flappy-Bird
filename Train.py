from './objects/Bird.py' import Bird
from Pipe import Pipe
from Base import Base
from Background import Background
from Environment import *

# Method to draw all objects to the window
def draw_window(objects):
    birds, base, pipes, bg, win, score = objects
    bg.draw(win)
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    for bird in birds:
        bird.draw(win)
    text = STATS_FONT.render(f"Score : {score}", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    pygame.display.update()

def eval_genomes(genomes, config):
    # Genes
    birds = []
    nets = []
    genes = []

    for _, gene in genomes:
        net = neat.nn.FeedForwardNetwork.create(gene, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        gene.fitness = 0
        genes.append(gene)

    # Initialize the object
    bg = Background()
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    objects = [birds, base, pipes, bg, win, score]

    # Game variables
    add_pipe = False
    running = True

    # Game loop
    while running:
        # Game FPS
        clock.tick(30)

        # Break after best gene
        if objects[5] >= 100:
            running = False
            break

        # Close game if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        # Get pipe in front and to check if any bird is alive
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            running = False
            break

        # Bird move 
        for x, bird in enumerate(birds):
            bird.move()
            genes[x].fitness += 0.1

            output = nets[x].activate((bird.y,
                                        abs(bird.y - pipes[pipe_ind].height),
                                        abs(bird.y - pipes[pipe_ind].bottom)))
            
            if output[0] > 0.5: 
                bird.jump()

        # Pipe movements 
        passed_pipes = []
        for pipe in pipes:
            # Check collision
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    genes[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    genes.pop(x)

                # Check if the pipe has passed the bird to initiate new pipe creation
                if not pipe.passed and pipe.x < bird.x : 
                    pipe.passed = True
                    add_pipe = True
            
            # Check if pipe has gone out of the window
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                passed_pipes.append(pipe)

            # Move Pipes
            pipe.move()

        # Adding new pipe 
        if  add_pipe:
            pipes.append(Pipe(700))
            objects[5] += 1
            for gene in genes:
                gene.fitness += 5
            add_pipe = False
        
        # Removing the pipes that have gone out of screen
        for pipe in passed_pipes:
            pipes.remove(pipe)

        # Moving the objects
        base.move()
        bg.move()
        
        # Check if bird has hit the ground
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y - bird.img.get_height() < 0:
                birds.pop(x)
                nets.pop(x)
                genes.pop(x)
        
        # Draw the objects
        draw_window(objects)
            
    
# Run NEAT
def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(eval_genomes, 10)
    # Save model
    file = open('model', 'wb')
    pickle.dump(winner, file)
    file.close()

    
# Calling main
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)