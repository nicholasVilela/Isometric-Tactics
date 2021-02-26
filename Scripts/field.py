import numpy, constants, re
from tile_entity import TileEntity
from sprite import Sprite
from location import Location
from raw_location import RawLocation
from offset import Offset


class Field:
    def __init__(self):
        self.map = self.construct_map(self.get_map_data())

    def update(self, layer):
        for y in range(0, self.map_width):
            for x in range(0, self.map_height):
                entity = self.map[y][x]
                entity.update(layer)

    def get_map_data(self):
        raw_terrain_map = open('map.txt').read()

        rows = raw_terrain_map.split('\n')

        map_data = list(map(lambda x: x.split(','), rows))

        return map_data        

    def construct_map(self, map_data):
        scale = 2
        
        self.map_height = len(map_data)
        self.map_width = len(map_data[0])

        map_result = numpy.empty((self.map_width, self.map_height), TileEntity)

        for y, row in enumerate(map_data):
            for x, raw_tile in enumerate(row):
                tiles_below = self.get_tile_depth(raw_tile)
                sub_tiles = []

                if (tiles_below != 0):
                    start_range = tiles_below if tiles_below < 0 else 0
                    end_range = tiles_below if tiles_below > 0 else 0
                    for z in range(start_range, end_range):
                        raw_sub_tile_terrain = self.get_sub_tile_terrain(raw_tile)[0]
                        raw_sub_tile = f'{z}{raw_sub_tile_terrain}'

                        sub_tile_entity = self.construct_tile_entity(x, y, raw_sub_tile, scale)  
                        sub_tiles.append(sub_tile_entity)         

                tile_entity = self.construct_tile_entity(x, y, raw_tile, scale, sub_tiles)

                map_result[x][y] = tile_entity

        return map_result

    def construct_tile_entity(self, x, y, tile, scale, sub_tiles = None):
        tile_terrain = self.get_tile_terrain(tile)
        tile_depth = self.get_tile_depth(tile)
        sprite = self.get_tile_sprite(tile, scale)
        raw_location = self.calculate_raw_location(x, y, scale, tile)
        location = Location(x, y, tile_depth, raw_location)
        entity = TileEntity(sprite, location, tile_terrain, sub_tiles)

        return entity

    def calculate_raw_location(self, x, y, scale, tile):
        x_offset = 10
        y_offset = 5
        start_width = 140
        start_height = self.get_tile_height(tile)

        raw_x = (start_width * scale) + (x * (x_offset * scale)) - (y * (x_offset * scale))
        raw_y = (start_height * scale) + (x * (y_offset * scale)) + (y * (y_offset * scale))
        offset = Offset(0, 0)

        return RawLocation(raw_x, raw_y, offset)

    def get_tile_height(self, tile):
        tile_depth = self.get_tile_depth(tile)
        tile_terrain_type = self.get_tile_terrain(tile)
        tile_height_offset = tile_depth * -12
        start_height = 82 if tile_terrain_type == constants.TERRAIN['w'] else 80

        return start_height + tile_height_offset

    def get_tile_depth(self, tile):
        if tile[0] == '-':
            return int(tile[0:2])
        return int(tile[0])

    def get_tile_terrain(self, tile):
        if tile[0] == '-':
            return constants.TERRAIN[f'{tile[2:]}']
        return constants.TERRAIN[f'{tile[1:]}']

    def get_tile_sprite(self, tile, scale):
        terrain_type = self.get_tile_terrain(tile)
        tile_sprite = constants.TILES[f'{terrain_type}']

        return Sprite(tile_sprite, scale)

    def get_sub_tile_terrain(self, tile):
        parent_tile_terrain = self.get_tile_terrain(tile)

        if parent_tile_terrain == constants.TERRAIN['g']:
            return constants.TERRAIN['d']
        
        return parent_tile_terrain

    def get_tile_for_location(self, x, y):
        if x == self.map_width:
            return self.map[0][y]
        elif y == self.map_height:
            return self.map[x][0]

        return self.map[x][y]
