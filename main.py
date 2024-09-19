import pygame, time, sys, math, random
from pygame.locals import *

PY_HEIGHT = 1000
PY_WIDTH = 1000
PY_NAME = "cool game"
FPS = 30
screen = pygame.display.set_mode((PY_WIDTH, PY_HEIGHT))
pygame.display.set_caption(PY_NAME)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)

    pygame.display.update()
