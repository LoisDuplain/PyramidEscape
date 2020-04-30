import pygame

from component.renderer.renderer import AnchorType
from entity.entity import Entity
from entity.entitypart import EntityPart
from level.camera import Camera
from entity.player.player import Player
import CONSTANTS


class Level:
    """
        CONSTRUCT
    """

    def __init__(self, level_name):
        self.level_name = level_name
        self.player = Player()

        self.camera = Camera()
        self.camera.set_x(self.player.get_world_x())
        self.camera.set_y(self.player.get_world_y())

        self.tiles = []

        self.debug = False

        self.entity = Entity()

        self.head_part = EntityPart("player-head.png")

        self.chest_part = EntityPart("player-chest.png")
        self.chest_part.set_anchor(AnchorType.TOP_MIDDLE)
        self.chest_part.set_offset_y(25)
        self.head_part.add_child(self.chest_part)

        self.entity.add_part(self.head_part)

    """
        METHODS
    """

    def render(self, screen):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                self.tiles[y][x].render(screen, self.camera)

        # TODO Render movable entities (Fireball etc)
        # TODO Render player
        self.player.render(screen, self.camera)
        # TODO Render particles
        # TODO Render HUD

        self.entity.render(screen, self.camera)

        if self.debug:
            pygame.draw.line(screen, pygame.Color(255, 255, 255), (CONSTANTS.CONSTANT_WINDOW_WIDTH / 2, 0), (CONSTANTS.CONSTANT_WINDOW_WIDTH / 2, CONSTANTS.CONSTANT_WINDOW_HEIGHT))
            pygame.draw.line(screen, pygame.Color(255, 255, 255), (0, CONSTANTS.CONSTANT_WINDOW_HEIGHT / 2), (CONSTANTS.CONSTANT_WINDOW_WIDTH, CONSTANTS.CONSTANT_WINDOW_HEIGHT / 2))

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
        self.head_part.add_angle(1)

        movement_speed = 5 * delta_time / 10
        if keys[pygame.K_d]:
            self.player.set_world_x(self.player.get_world_x() + movement_speed)
            self.camera.set_x(self.player.get_world_x())
        if keys[pygame.K_a]:
            self.player.set_world_x(self.player.get_world_x() - movement_speed)
            self.camera.set_x(self.player.get_world_x())
        if keys[pygame.K_w]:
            self.player.set_world_y(self.player.get_world_y() - movement_speed)
            self.camera.set_y(self.player.get_world_y())
        if keys[pygame.K_s]:
            self.player.set_world_y(self.player.get_world_y() + movement_speed)
            self.camera.set_y(self.player.get_world_y())
        pass

    def events(self, event):
        # Events
        pass

    def key_pressed(self, key):
        if key == pygame.K_COMMA:
            self.debug = not self.debug
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

    def set_debug(self, new_debug):
        self.debug = new_debug

    def is_debug(self):
        return self.debug
