import pygame, time, sys, math, random
from pygame.locals import *

PY_HEIGHT = 1000
PY_WIDTH = 1000
PY_NAME = "cool game"
FPS = 60
screen = pygame.display.set_mode((PY_WIDTH, PY_HEIGHT))
pygame.display.set_caption(PY_NAME)
clock = pygame.time.Clock()

WORLD_X = 0
WORLD_Y = 200

light = False
can_light = True

class images():
    flashlight = pygame.image.load("Images/flashlight.png")
    flashlight_rect = flashlight.get_rect(center=(PY_WIDTH // 2, PY_HEIGHT // 2))

class colors():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

class char():
    c_height = PY_HEIGHT // 2
    c_width = PY_WIDTH // 2
    c_size = 50
    rotation = 0

    g_heightP = PY_HEIGHT // 2 - 25
    g_widthP = PY_HEIGHT // 2 - 25
    g_heightS = 25
    g_widthS = 50

    SPEED = 5

def draw_shape(shape, posX, posY):
    if shape == "straight":
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY, 500, 50))
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY - 400, 500, 50))
    elif shape == "straight2":
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY, 1000, 50))
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY - 400, 1000, 50))
    elif shape == "straight2_END":
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY, 1000, 50))
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX, WORLD_Y + posY - 400, 1000, 50))
        pygame.draw.rect(screen, (colors.WHITE), (WORLD_X - posX + 1000, WORLD_Y + posY - 400, 50, 450))
    else:
        print("ERROR, WRONG SHAPE")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx = mouse_x - char.g_widthP
    dy = mouse_y - char.g_heightP
    angle = math.degrees(math.atan2(-dy, dx))

    print(WORLD_X, WORLD_Y, angle, light)

    if keys[pygame.K_w]:
        WORLD_Y += char.SPEED
    if keys[pygame.K_s]:
        WORLD_Y -= char.SPEED
    if keys[pygame.K_a]:
        WORLD_X += char.SPEED
    if keys[pygame.K_d]:
        WORLD_X -= char.SPEED
    if keys[pygame.K_f]:
        if can_light:
            light = not light
            can_light = False
    if not keys[pygame.K_f]:
        can_light = True

    pygame.draw.circle(screen, (100, 100, 100), (char.c_width, char.c_height), char.c_size)

    draw_shape("straight2_END", 300, 500)

    if light:
        rotated_flashlight = pygame.transform.rotate(images.flashlight, angle + 180 + 90)
        rotated_rect = rotated_flashlight.get_rect(center=images.flashlight_rect.center)
        screen.blit(rotated_flashlight, rotated_rect.topleft)

    pygame.display.flip()
