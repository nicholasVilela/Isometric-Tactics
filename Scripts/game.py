import pygame, constants, state
from cursor_entity import CursorEntity
from sprite import Sprite
from location import Location
from raw_location import RawLocation
from offset import Offset

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.layers = self.construct_layers()
        state.cursor = self.construct_cursor()

    def update(self):
        self.update_events()
        self.update_entities()

    def update_entities(self):
        state.field.update(self.layers['midground'])

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.end_game()
            else:
                state.cursor.update(self.layers['foreground'], event)
        
        state.cursor.update(self.layers['foreground'])

    def construct_layers(self):
        background = pygame.Surface((constants.SCREEN_SIZE[0], constants.SCREEN_SIZE[1]))

        midground = pygame.Surface((constants.SCREEN_SIZE[0], constants.SCREEN_SIZE[1]))
        midground.set_colorkey(constants.COLORS['black'])

        foreground = pygame.Surface((constants.SCREEN_SIZE[0], constants.SCREEN_SIZE[1]))
        foreground.set_colorkey(constants.COLORS['black'])

        layers = {
            'background': background,
            'midground' : midground,
            'foreground': foreground
        }

        return layers

    def construct_cursor(self):
        starting_tile = state.field.get_tile_for_location(0, 0)

        sprite = Sprite(constants.SPRITES['cursor'], 2)
        offset = Offset(0, -40)
        raw_location = RawLocation(starting_tile.location.raw.x, starting_tile.location.raw.y, offset)
        location = Location(starting_tile.location.x, starting_tile.location.y, starting_tile.location.z, raw_location)

        return CursorEntity(sprite, location, constants.CONTROLLER)

    def end_game(self):
        self.running = False