import pygame

from level.camera import Camera
from level.tile import Tile, TileType
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

        self.generate_tiles()
        
        self.debug = False

    def generate_tiles(self):
        # TODO Load chars into the file that contains level_name in his file name and then, generate tiles
        file = open("level/files/" + self.level_name, "r")
        y = 0
        for line in file:
            x = 0
            x_tiles = []
            for char in line:
                tile_type = None
                if char == "0":
                    tile_type = TileType.AIR
                elif char == "1":
                    tile_type = TileType.GROUND
                elif char == "2":
                    tile_type = TileType.SPIKE
                else:
                    break
                x_tiles.append(Tile(tile_type, x, y))
                x += 1
            self.tiles.append(x_tiles)
            y += 1
        file.close()

        file = open("level/files/" + self.level_name, "r")
        y = 0
        for line in file:
            x = len(line)-2
            """
                Pourquoi -2 ?
                len(line) renvoie le nombre de caractères sur une ligne mais nous on veut compter à partir de 0 donc cela fait déjà -1
                Ensuite on a le \n à la fin qu'il faut supprimer donc encore -1
                
                Donc -1 - 1 = -2
            """
            x_tiles = []
            for char in line:
                tile_type = None
                if char == "0":
                    tile_type = TileType.AIR
                elif char == "1":
                    tile_type = TileType.GROUND
                elif char == "2":
                    tile_type = TileType.SPIKE
                else:
                    break
                x_tiles.append(Tile(tile_type, x, y+9))
                x -= 1
            self.tiles.append(x_tiles)
            y += 1
        file.close()

    """
        METHODS
    """

    def render(self, screen):
        # TODO Render tiles
        for y in range (len(self.tiles)):
            for x in range (len(self.tiles[y])):
                self.tiles[y][x].render(screen, self.camera)

        # TODO Render movable entities (Fireball etc)
        # TODO Render player
        self.player.render(screen, self.camera)
        # TODO Render particles
        # TODO Render HUD

        if self.debug:
            pygame.draw.line(screen, pygame.Color(255,255,255), (CONSTANTS.CONSTANT_WINDOW_WIDTH/2, 0), (CONSTANTS.CONSTANT_WINDOW_WIDTH/2, CONSTANTS.CONSTANT_WINDOW_HEIGHT))
            pygame.draw.line(screen, pygame.Color(255,255,255), (0, CONSTANTS.CONSTANT_WINDOW_HEIGHT/2), (CONSTANTS.CONSTANT_WINDOW_WIDTH, CONSTANTS.CONSTANT_WINDOW_HEIGHT/2))
            

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
            self.player.set_world_x(self.player.get_world_x() + delta_time)
            self.camera.set_x(self.player.get_world_x())
        if keys[pygame.K_a]:
            self.player.set_world_x(self.player.get_world_x() - delta_time)
            self.camera.set_x(self.player.get_world_x())
        if keys[pygame.K_w]:
            self.player.set_world_y(self.player.get_world_y() - delta_time)
            self.camera.set_y(self.player.get_world_y())
        if keys[pygame.K_s]:
            self.player.set_world_y(self.player.get_world_y() + delta_time)
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
