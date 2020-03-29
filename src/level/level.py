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
        self.player.render(screen)
        # TODO Render particles
        # TODO Render HUD

        # TEST PLAYER SHAPE
        test_player = False
        if test_player:
            # - head
            pygame.draw.rect(screen, pygame.Color(48, 51, 107), pygame.Rect(100, 100, 30, 30))
            # - chest
            pygame.draw.rect(screen, pygame.Color(235, 77, 75), pygame.Rect(100, 130, 30, 50))
            # - left arm
            pygame.draw.rect(screen, pygame.Color(106, 176, 76), pygame.Rect(85, 130, 15, 50))
            # - right arm
            pygame.draw.rect(screen, pygame.Color(34, 166, 179), pygame.Rect(130, 130, 15, 50))
            # - left leg
            pygame.draw.rect(screen, pygame.Color(186, 220, 88), pygame.Rect(100, 180, 15, 50))
            # - right leg
            pygame.draw.rect(screen, pygame.Color(126, 214, 223), pygame.Rect(115, 180, 15, 50))
        pass

    def update(self, delta_time, keys):
        # TODO Update player pos
        # TODO Update camera pos
        # TODO Update particle systems
        # TODO Update movable entities
        if keys[pygame.K_d]:
            self.player.set_world_x(self.player.get_world_x()+delta_time/10)
        if keys[pygame.K_a]:
            self.player.set_world_x(self.player.get_world_x()-delta_time/10)
        pass

    def events(self, event):
        # Events
        pass

    def key_pressed(self, key):
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
