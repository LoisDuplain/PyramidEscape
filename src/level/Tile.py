from enum import Enum
from renderer.RenderableObject import RenderableObject


class TileType(Enum):
    GROUND = "ground.png"
    SPIKE = "spike.png"


class Tile(RenderableObject):
    CONSTANT_TILE_WIDTH = 30
    CONSTANT_TILE_HEIGHT = 30

    """
        CONSTRUCT
    """

    def __init__(self, tile_type, x, y):
        super.__init__(tile_type.value)
        self.tile_type = tile_type
        self.x = x
        self.y = y

    """
        METHODS
    """

    def render(self, screen):
        # TODO Render tile
        pass

    """
        GETTERS AND SETTERS
    """

    def get_tile_type(self):
        return self.tile_type

    def set_tile_type(self, new_tile_type):
        self.tile_type = new_tile_type

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.y = y