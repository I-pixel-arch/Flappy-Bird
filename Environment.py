import pygame
import neat
import time
import os
import random
pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 550, 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bird1.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bird2.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bird2.png')))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bg.png')))
STATS_FONT = pygame.font.SysFont("comicsans", 50)