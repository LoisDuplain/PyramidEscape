import math

import Utils
from renderer.RenderableObject import RenderableObject, AnchorType


class Member(RenderableObject):
    """
        CONSTRUCT
    """

    def __init__(self, character_velocity_remover, sprite, anchor_type, fixed_to=None):
        super().__init__(sprite)
        super().set_anchor(anchor_type)
        # super().set_rendering_anchor(True)

        self.player_velocity_remover = character_velocity_remover

        self.fixed_to = fixed_to

        self.offset_x = 0
        self.offset_y = 0

        self.last_render_x = 0
        self.last_render_y = 0

    """
        METHODS
    """

    def render(self, screen, world_x, world_y, angle=0):
        render_x = world_x
        render_y = world_y
        if self.fixed_to is not None:
            render_x += self.fixed_to.get_last_render_x() + self.offset_x
            render_y += self.fixed_to.get_last_render_y() + self.offset_y

        self.last_render_x = render_x
        self.last_render_y = render_y

        super().render(screen, render_x, render_y, angle)

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


class HeadMember(Member):
    def __init__(self):
        super().__init__(0, "player-head.png", AnchorType.BOTTOM_MIDDLE)


class ChestMember(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-chest.png", AnchorType.MIDDLE, fixed_to)
        super().set_offset_y(25)


class LeftArm(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-left-arm.png", AnchorType.TOP_RIGHT, fixed_to)
        super().set_offset_x(-fixed_to.get_original_width() / 2 + 1)
        super().set_offset_y(-fixed_to.get_original_height() / 2 + 1)


class RightArm(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-right-arm.png", AnchorType.TOP_LEFT, fixed_to)
        super().set_offset_x(fixed_to.get_original_width()/2)
        super().set_offset_y(-fixed_to.get_original_height() / 2 + 1)


class LeftLeg(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-left-leg.png", AnchorType.TOP_MIDDLE, fixed_to)
        super().set_offset_x(-fixed_to.get_original_width() / 4)
        super().set_offset_y(fixed_to.get_original_height() / 2)


class RightLeg(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-right-leg.png", AnchorType.TOP_MIDDLE, fixed_to)
        super().set_offset_x(fixed_to.get_original_width() / 4)
        super().set_offset_y(fixed_to.get_original_height() / 2)


class Player:
    """
        CONSTRUCT
    """

    def __init__(self):
        self.world_x = 35
        self.world_y = 130

        self.head_member = HeadMember()

        self.chest_member = ChestMember(self.head_member)

        self.left_arm_member = LeftArm(self.chest_member)
        self.right_arm_member = RightArm(self.chest_member)

        self.left_leg_member = LeftLeg(self.chest_member)
        self.right_leg_member = RightLeg(self.chest_member)

        self.start_at = Utils.get_current_time_millis()

    """
        METHODS
    """

    def render(self, screen):
        self.head_member.render(screen, self.world_x, self.world_y, 0)

        self.chest_member.render(screen, 0, 0, 0)

        self.left_arm_member.render(screen, 0, 0, Utils.map(math.cos((Utils.get_current_time_millis()-self.start_at)/300), -1, 1, -3, 2))
        self.right_arm_member.render(screen, 0, 0, Utils.map(math.cos((Utils.get_current_time_millis()-self.start_at)/350), -1, 1, -3, 2))

        self.left_leg_member.render(screen, 0, 0, 0)
        self.right_leg_member.render(screen, 0, 0, 0)

    """
        GETTERS AND SETTERS
    """

    def get_world_x(self):
        return self.world_x

    def set_world_x(self, new_world_x):
        self.world_x = new_world_x

    def get_world_y(self):
        return self.world_y

    def set_world_y(self, new_world_y):
        self.world_y = new_world_y
