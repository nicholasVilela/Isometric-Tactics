import state, numpy
from entity import Entity
from raw_location import RawLocation
from location import Location

class CursorEntity(Entity):
    def __init__(self, sprite, location, controller):
        super().__init__(sprite, location)
        self.controller = controller

    def update(self, layer, event = None):
        self.controller.update(event)
        self.update_movement()
        self.update_map()
        self.render(layer)

    def update_movement(self):
        target_location_x = self.location.x
        target_location_y = self.location.y

        if self.controller.move_left.pressed:
            target_location_x -= 1
        elif self.controller.move_right.pressed:
            target_location_x += 1
        elif self.controller.move_up.pressed:
            target_location_y -= 1
        elif self.controller.move_down.pressed:
            target_location_y += 1
            

        self.location = self.change_location(target_location_x, target_location_y)

    def change_location(self, x, y):
        target_tile = state.field.get_tile_for_location(x, y)
        target_raw_x_location = target_tile.location.raw.x + self.location.raw.offset.x
        target_raw_y_location = target_tile.location.raw.y + self.location.raw.offset.y
        target_raw_location = RawLocation(target_tile.location.raw.x + self.location.raw.offset.x, target_tile.location.raw.y + target_tile.location.raw.offset.y, self.location.raw.offset)
        target_location = Location(target_tile.location.x, target_tile.location.y, target_tile.location.z, target_raw_location)

        return target_location

    def update_map_file(self, map_matrix):
        target_map_file = ''

        for y, row in enumerate(map_matrix):
            for x, col in enumerate(row):
                target_map_file += map_matrix[y][x]
                target_map_file += ','
            if (y + 1) != len(map_matrix[0]):
                target_map_file += '\n'
            
        target_map_file = target_map_file.replace(',\n', '\n')
        target_map_file = target_map_file.rstrip(',')

        with open('map.txt', 'w') as f:
            f.truncate(0)
            f.write(target_map_file)

    def update_map(self):
        if self.controller.rotate_left.pressed:
            terrain_map = state.field.get_map_data()
            rotated_terrain_map = numpy.rot90(terrain_map)
            state.field.map = state.field.construct_map(rotated_terrain_map)

            self.update_map_file(rotated_terrain_map)
        elif self.controller.rotate_right.pressed:
            terrain_map = state.field.get_map_data()
            rotated_terrain_map = numpy.rot90(terrain_map, 3)
            state.field.map = state.field.construct_map(rotated_terrain_map)

            self.update_map_file(rotated_terrain_map)
            
            