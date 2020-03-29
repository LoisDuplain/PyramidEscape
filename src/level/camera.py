import CONSTANTS


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def get_render_x(self, x):
        return CONSTANTS.CONSTANT_WINDOW_WIDTH/2 - self.x + x
    
    def sub_x(self, x_to_sub):
        self.x -= x_to_sub

    def add_x(self, x_to_add):
        self.x += x_to_add

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y
        
    def get_render_y(self, y):
        return CONSTANTS.CONSTANT_WINDOW_HEIGHT/2 - self.y + y

    def sub_y(self, y_to_sub):
        self.y -= y_to_sub

    def add_y(self, y_to_add):
        self.y += y_to_add

    def set_y(self, new_y):
        self.y = new_y
