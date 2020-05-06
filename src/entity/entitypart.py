import math

from component.renderer.renderer import Renderer


class EntityPart(Renderer):

    def __init__(self, image):
        super().__init__(image)

        self.parent = None
        self.children = []

        self.offset_x = 0
        self.offset_y = 0

        self.angle = 0

    def render(self, screen, camera, x=0, y=0, angle=0):
        super().render(screen, camera, x+self.offset_x, y+self.offset_y, self.angle + angle)
        for child in self.children:
            child.render(screen, camera, x + self.offset_x, y + self.offset_y, self.angle + angle)

    def update(self, delta_time, keys):
        pass

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def set_offset_x(self, offset_x):
        self.offset_x = offset_x

    def add_offset_x(self, offset_x):
        self.offset_x += offset_x

    def sub_offset_x(self, offset_x):
        self.offset_x -= offset_x

    def get_offset_x(self):
        return self.offset_x

    def set_offset_y(self, offset_y):
        self.offset_y = offset_y

    def add_offset_y(self, offset_y):
        self.offset_y += offset_y

    def sub_offset_y(self, offset_y):
        self.offset_y -= offset_y

    def get_offset_y(self):
        return self.offset_y

    def set_angle(self, angle):
        self.angle = angle

    def add_angle(self, angle):
        self.angle += angle

    def get_angle(self):
        return self.angle
