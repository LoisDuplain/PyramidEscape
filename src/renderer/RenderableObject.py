import math
from enum import Enum

import pygame

import Utils


def loadImage(imageName):
    image_path = "resources/img/" + imageName
    try:
        image = pygame.image.load(image_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', image_path)
        raise SystemExit(message)
    return image


class RenderableObject(pygame.sprite.Sprite):
    """
        CONSTRUCT
    """

    def __init__(self, image):
        super(RenderableObject, self).__init__()

        self.original_image = loadImage(image)
        self.original_width = self.original_image.get_width()
        self.original_height = self.original_image.get_height()

        self.current_image = self.original_image
        self.current_width = self.current_image.get_width()
        self.current_height = self.current_image.get_height()

        self.set_anchor(AnchorType.MIDDLE)
        self.anchor_x = self.original_width / 2
        self.anchor_y = self.original_height / 2

        self.rect = self.current_image.get_rect()

        self.render_anchor = False
        self.render_border = False

    """
        METHODS
    """

    def render(self, screen, x, y, angle=0):
        screen.blit(self.current_image, self.rect)
        self.compute_center_point(screen, x, y, angle)
        if self.render_anchor:
            pygame.draw.line(screen, pygame.Color(0, 0, 255), (x - 5, y), (x + 5, y))
            pygame.draw.line(screen, pygame.Color(255, 0, 0), (x, y - 5), (x, y + 5))
        if self.render_border:
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), self.rect, 1)

    def compute_center_point(self, screen, x, y, angle):
        self.set_current_image(pygame.transform.rotozoom(self.original_image, angle, 1))
        self.rect = self.get_current_image().get_rect()

        dx = self.original_width / 2 - self.anchor_x
        dy = self.original_height / 2 - self.anchor_y
        d = Utils.calculate_distance(self.anchor_x, self.anchor_y, self.anchor_x + dx, self.anchor_y + dy)

        a = math.atan2(dy, dx)
        a -= math.radians(angle)
        # print("Dx:", dx, "| Dy:", dy, "| D:", d, "| Angle (radians):", a, "| Angle (degrees):", math.degrees(a))

        nx = math.cos(a)*d
        ny = math.sin(a)*d

        if self.render_anchor:
            pygame.draw.line(screen, pygame.Color(200, 66, 245), (x, y), (x + nx, y))
            pygame.draw.line(screen, pygame.Color(200, 66, 245), (x + nx, y), (x + nx, y + ny))

        self.rect.center = (x + nx, y + ny)

    """
        GETTERS AND SETTERS
    """

    def get_original_image(self):
        return self.original_image

    def set_original_image(self, new_original_image):
        self.original_image = new_original_image
        self.original_width = new_original_image.get_width()
        self.original_height = new_original_image.get_height()
        self.rect = self.current_image.get_rect()

    def get_original_width(self):
        return self.original_width

    def get_original_height(self):
        return self.original_height

    def get_current_image(self):
        return self.current_image

    def set_current_image(self, new_current_image):
        self.current_image = new_current_image
        self.current_width = new_current_image.get_width()
        self.curren_height = new_current_image.get_height()

    def get_current_width(self):
        return self.current_width

    def get_current_height(self):
        return self.current_height

    def get_anchor_x(self):
        return self.anchor_x

    def set_anchor_x(self, new_anchor_x):
        self.anchor_x = new_anchor_x

    def get_anchor_y(self):
        return self.anchor_y

    def set_anchor_y(self, new_anchor_y):
        self.anchor_y = new_anchor_y

    def set_anchor(self, anchor_type):
        if anchor_type == AnchorType.MIDDLE:
            self.set_anchor_x(self.get_original_width() / 2)
            self.set_anchor_y(self.get_original_height() / 2)
        elif anchor_type == AnchorType.TOP_LEFT:
            self.set_anchor_x(0)
            self.set_anchor_y(0)
        elif anchor_type == AnchorType.TOP_MIDDLE:
            self.set_anchor_x(self.get_original_width() / 2)
            self.set_anchor_y(0)
        elif anchor_type == AnchorType.TOP_RIGHT:
            self.set_anchor_x(self.get_original_width())
            self.set_anchor_y(0)
        elif anchor_type == AnchorType.MIDDLE_RIGHT:
            self.set_anchor_x(self.get_original_width())
            self.set_anchor_y(self.get_original_height() / 2)
        elif anchor_type == AnchorType.BOTTOM_RIGHT:
            self.set_anchor_x(self.get_original_width())
            self.set_anchor_y(self.get_original_height())
        elif anchor_type == AnchorType.BOTTOM_MIDDLE:
            self.set_anchor_x(self.get_original_width() / 2)
            self.set_anchor_y(self.get_original_height())
        elif anchor_type == AnchorType.BOTTOM_LEFT:
            self.set_anchor_x(0)
            self.set_anchor_y(self.get_original_height())
        elif anchor_type == AnchorType.MIDDLE_LEFT:
            self.set_anchor_x(0)
            self.set_anchor_y(self.get_original_height() / 2)

    def is_rendering_anchor(self):
        return self.render_anchor

    def set_rendering_anchor(self, state):
        self.render_anchor = state

    def is_rendering_border(self):
        return self.render_border

    def set_rendering_border(self, state):
        self.render_border = state


class AnchorType(Enum):
    MIDDLE = 0
    TOP_LEFT = 1
    TOP_MIDDLE = 2
    TOP_RIGHT = 3
    MIDDLE_RIGHT = 4
    BOTTOM_RIGHT = 5
    BOTTOM_MIDDLE = 6
    BOTTOM_LEFT = 7
    MIDDLE_LEFT = 8
