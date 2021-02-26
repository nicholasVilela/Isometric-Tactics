import pygame
from controller import Controller
from button import Button


SCREEN_SIZE = (600, 480)
DISPLAY_SIZE = (300, 200)
SCREEN_FILL = (134,97,97)
FRAMERATE = 60

CONTROLLER = Controller(
    Button('Left', pygame.K_LEFT),
    Button('Right', pygame.K_RIGHT),
    Button('Up', pygame.K_UP),
    Button('Down', pygame.K_DOWN),
    Button('Rotate Left', pygame.K_q),
    Button('Rotate Right', pygame.K_e))

COLORS = { 
    'black': (0, 0, 0)
}

SPRITES = {
    'cursor': '../Sprites/cursor.png'
}

TILES = {
    'empty': '../Sprites/empty.png',
    'grass': '../Sprites/grass.png',
    'water': '../Sprites/water.png',
    'sand' : '../Sprites/sand.png',
    'dirt': '../Sprites/dirt.png'
}

TERRAIN = {
    'e': 'empty',
    'g': 'grass',
    'w': 'water',
    's': 'sand',
    'd': 'dirt'
}