from entity import Entity

class TileEntity(Entity):
    def __init__(self, sprite, location, terrain_type, sub_tiles):
        super().__init__(sprite, location)
        self.terrain_type = terrain_type
        self.sub_tiles = sub_tiles

    def update(self, layer):
        for tile in self.sub_tiles:
            tile.render(layer)
        self.render(layer)