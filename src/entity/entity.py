class Entity:

    def __init__(self):
        self.parts = []

        self.world_x = 0
        self.world_y = 0
        self.angle = 0

    def render(self, screen, camera):
        for part in self.parts:
            part.render(screen, camera, x=self.world_x, y=self.world_y)

    def update(self, delta_time, keys):
        pass

    def add_part(self, entity_part):
        self.parts.append(entity_part)

    def get_parts(self):
        return self.parts

    def set_world_x(self, world_x):
        self.world_x = world_x

    def add_world_x(self, world_x):
        self.world_x += world_x

    def sub_world_x(self, world_x):
        self.world_x -= world_x

    def get_world_x(self):
        return self.world_x

    def set_world_y(self, world_y):
        self.world_y = world_y

    def add_world_y(self, world_y):
        self.world_y += world_y

    def sub_world_y(self, world_y):
        self.world_y -= world_y

    def get_world_y(self):
        return self.world_y

    def set_angle(self, angle):
        self.angle = angle

    def add_angle(self, angle):
        self.angle += angle

    def sub_angle(self, angle):
        self.angle -= angle

    def get_angle(self):
        return self.angle