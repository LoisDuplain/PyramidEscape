from enum import Enum
from renderer.RenderableObject import RenderableObject, AnchorType


class TileType(Enum):
    AIR = "air.png"
    GROUND = "ground.png"
    SPIKE = "spike.png"


class Tile(RenderableObject):
    CONSTANT_TILE_WIDTH_FHD = 60
    CONSTANT_TILE_HEIGHT_FHD = 60

    """
        CONSTRUCT
    """

    def __init__(self, tile_type, x, y):
        super().__init__(tile_type.value)
        super().set_anchor(AnchorType.TOP_LEFT)
        self.tile_type = tile_type
        self.x = x
        self.y = y

    """
        METHODS
    """

    def render(self, screen, camera):
        super().render(screen, self.x*self.CONSTANT_TILE_WIDTH_FHD, self.y*self.CONSTANT_TILE_HEIGHT_FHD, camera)
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
        self.y = new_y