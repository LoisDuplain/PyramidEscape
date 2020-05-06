def is_in(vx, vy, x, y, width, height):
    if x <= vx <= x + width and y <= vy <= y + height:
        return True
    else:
        return False


class Collider():

    def __init__(self, entity_parent, width, height, offset_x=0, offset_y=0):
        self.entity_parent = entity_parent
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y

    def check_collisions(self, entities):
        __pos_x = self.entity_parent.get_world_x() + self.offset_x
        __pos_y = self.entity_parent.get_world_y() + self.offset_y

        __top_left_corner_x = __pos_x
        __top_left_corner_y = __pos_y

        __bottom_left_corner_x = __pos_x
        __bottom_left_corner_y = __pos_y + self.height

        __top_right_corner_x = __pos_x + self.width
        __top_right_corner_y = __pos_y

        __bottom_right_corner_x = __pos_x + self.width
        __bottom_right_corner_y = __pos_y + self.height

        for entity in entities:
            for collider in entity.get_colliders():
                collides = False

                pos_x = entity.get_world_x() + collider.get_offset_x()
                pos_y = entity.get_world_y() + collider.get_offset_y()

                if is_in(__top_left_corner_x, __top_left_corner_y, pos_x, pos_y, collider.get_width(), collider.get_height()):
                    collides = True
                elif is_in(__bottom_left_corner_x, __bottom_left_corner_y, pos_x, pos_y, collider.get_width(), collider.get_height()):
                    collides = True
                elif is_in(__top_right_corner_x, __top_right_corner_y, pos_x, pos_y, collider.get_width(), collider.get_height()):
                    collides = True
                elif is_in(__bottom_right_corner_x, __bottom_right_corner_y, pos_x, pos_y, collider.get_width(), collider.get_height()):
                    collides = True

    def get_entity_parent(self):
        return self.entity_parent

    def set_entity_parent(self, entity_parent):
        self.entity_parent = entity_parent

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_offset_x(self):
        return self.offset_x

    def set_offset_x(self, offset_x):
        self.offset_x = offset_x

    def get_offset_y(self):
        return self.offset_y

    def set_offset_y(self, offset_y):
        self.offset_y = offset_y
