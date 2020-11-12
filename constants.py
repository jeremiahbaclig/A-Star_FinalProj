# Jeremiah Baclig - last edit: 4/24/2020 @4PM
import pygame

# Testing out different colors for grid
WHITE = (255, 255, 255)
BLACK = (35, 35, 70)
SEA_GREEN = (30, 155, 155)
RED = (220, 60, 60)
LIGHT_RED = (255, 70, 70)
BLUE = (50, 50, 112)
VIOLET_RED = (199, 21, 133)
PINK = (255, 105, 180)
SKY_BLUE = (0, 191, 255)
POWDER_BLUE = (127, 212, 255)
GREEN = (0, 255, 0)

GRID = [[1] * 100 for n in range(100)]  # [x, y]
GRID2 = [[1] * 200 for n in range(200)]
GRID3 = [[1] * 300 for n in range(300)]

PATH = []
PATH_DIST = []
OBSTACLES = []

W = 8
W2 = 4
W3 = 2 + (2/3)
WIDTH = 800
HEIGHT = 800
END = False

START = (0, 0)
ENDING = (792, 792)
ENDING2 = (796, 796)
ENDING3 = (799.9999999999973, 797.3333333333306)
FINAL = (0, 0)
END_3X = 799.9999999999973
END_3Y = 797.3333333333306

SUM = 0

W0 = 9
W1 = 1

P10 = 5
P20 = 10
P30 = 15

INFLATION = 10

button110 = pygame.Rect(810, 100, 50, 50)
button120 = pygame.Rect(865, 100, 50, 50)
button130 = pygame.Rect(920, 100, 50, 50)
button210 = pygame.Rect(810, 300, 50, 50)
button220 = pygame.Rect(865, 300, 50, 50)
button230 = pygame.Rect(920, 300, 50, 50)
button310 = pygame.Rect(810, 500, 50, 50)
button320 = pygame.Rect(865, 500, 50, 50)
button330 = pygame.Rect(920, 500, 50, 50)
button_quit = pygame.Rect(865, 700, 50, 50)
