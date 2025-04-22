#https://youtu.be/Y_p1u1qiI6c
#Had issue with it not reading the png file correctly->professor tried to fix it and couldn't
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 640, 512
GRID_SIZE = 32
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desktop/mole.png")
mole_image = pygame.image.load("mole.png")
mole_rect = mole_image.get_rect()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (WIDTH, y))

def place_mole():
    x = random.randrange(0, GRID_WIDTH) * GRID_SIZE
    y = random.randrange(0, GRID_HEIGHT) * GRID_SIZE

def game_loop():
    place_mole()
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        draw_grid()

        pygame.display.flip()

if __name__ == '__main__':
    game_loop()
