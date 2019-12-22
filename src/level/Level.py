import pygame

from Camera import Camera
from player.Player import Player
from renderer.RenderableObject import RenderableObject, AnchorType


class Level:
    """
        CONSTRUCT
    """

    def __init__(self, level_name):
        self.level_name = level_name
        self.player = Player()
        self.camera = Camera()
        self.tiles = []

        self.angle = 0

        self.at = AnchorType.TOP_MIDDLE
        self.test_render_image = RenderableObject("player-head.png")
        self.test_render_image.set_anchor(self.at)

        self.generate_tiles()

    def generate_tiles(self):
        # TODO Load chars into the file that contains level_name in his file name and then, generate tiles
        """
            PART OF CODE EXAMPLE:
                if char==1:
                    self.tiles.append(Tile(TileType.GROUND, 0, 0))
        """
        pass

    """
        METHODS
    """

    def render(self, screen):
        # TODO Render tiles
        # TODO Render movable entities (Fireball etc)
        # TODO Render player
        # TODO Render particles
        # TODO Render HUD

        pygame.draw.line(screen, pygame.Color(255, 255, 255), (50, 0), (50, 540))
        pygame.draw.line(screen, pygame.Color(255, 255, 255), (0, 70), (960, 70))
        self.test_render_image.render(screen, 50, 70, self.angle)
        pass

    def update(self, delta_time):
        # TODO Update player pos
        # TODO Update camera pos
        # TODO Update particle systems
        # TODO Update movable entities
        self.angle += 1
        pass

    def events(self, event):
        # Events
        pass

    def key_down(self, keys):
        # TODO Detect key entries
        pass

    def key_pressed(self, key):
        if key == pygame.K_a:
            self.at = AnchorType(self.at.value + 1)
            self.test_render_image.set_anchor(self.at)
        pass

    def key_released(self, key):
        pass

    """
        GETTERS AND SETTERS
    """

    def get_level_name(self):
        return self.level_name

    def set_level_name(self, new_level_name):
        self.level_name = new_level_name

    def get_player(self):
        return self.player

    def set_player(self, new_player):
        self.player = new_player

    def get_tiles(self):
        return self.tiles

    def set_tiles(self, new_tiles):
        self.tiles = new_tiles
