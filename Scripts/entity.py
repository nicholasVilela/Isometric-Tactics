class Entity:
    def __init__(self, sprite, location):
        self.sprite = sprite
        self.location = location

    def update(self, layer):
        self.render(layer)

    def render(self, layer):
        image = self.sprite.as_scale()
        target_location = (self.location.raw.x + self.location.raw.offset.x, self.location.raw.y + self.location.raw.offset.y)
        layer.blit(image, target_location)