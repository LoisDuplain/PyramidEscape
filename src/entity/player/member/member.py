from component.renderer.renderer import Renderer


class Member(Renderer):
    """
        CONSTRUCT
    """

    def __init__(self, character_velocity_remover, sprite, anchor_type, fixed_to=None):
        super().__init__(sprite)
        super().set_anchor(anchor_type)
        super().set_rendering_anchor(False)
        super().set_rendering_border(False)

        self.player_velocity_remover = character_velocity_remover

        self.fixed_to = fixed_to

        self.offset_x = 0
        self.offset_y = 0

        self.last_render_x = 0
        self.last_render_y = 0

    """
        METHODS
    """

    def render(self, screen, camera, world_x, world_y, angle=0):
        render_x = world_x
        render_y = world_y
        if self.fixed_to is not None:
            render_x += self.fixed_to.get_last_render_x() + self.offset_x
            render_y += self.fixed_to.get_last_render_y() + self.offset_y

        self.last_render_x = render_x
        self.last_render_y = render_y

        super().render(screen, camera, render_x, render_y, angle)

    """
        GETTERS AND SETTERS
    """

    def get_player_velocity_remover(self):
        return self.character_velocity_remover

    def set_player_velocity_remover(self, new_player_velocity_remover):
        self.player_velocity_remover = new_player_velocity_remover

    def get_fixed_to(self):
        return self.fixed_to

    def set_fixed_to(self, new_fixed_to):
        self.fixed_to = new_fixed_to

    def get_offset_x(self):
        return self.offset_x

    def set_offset_x(self, new_offset_x):
        self.offset_x = new_offset_x

    def get_offset_y(self):
        return self.offset_y

    def set_offset_y(self, new_offset_y):
        self.offset_y = new_offset_y

    def get_last_render_x(self):
        return self.last_render_x

    def get_last_render_y(self):
        return self.last_render_y