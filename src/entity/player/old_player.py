import math

import utils
from entity.player.member.chestmember import ChestMember
from entity.player.member.headmember import HeadMember
from entity.player.member.leftarmmember import LeftArmMember
from entity.player.member.leftlegmember import LeftLegMember
from entity.player.member.rightarmmember import RightArmMember
from entity.player.member.rightlegmember import RightLegMember


class Player:
    """
        CONSTRUCT
    """

    def __init__(self):
        self.world_x = 350
        self.world_y = 130

        self.head_member = HeadMember()

        self.chest_member = ChestMember(self.head_member)

        self.left_arm_member = LeftArmMember(self.chest_member)
        self.right_arm_member = RightArmMember(self.chest_member)

        self.left_leg_member = LeftLegMember(self.chest_member)
        self.right_leg_member = RightLegMember(self.chest_member)

        self.start_at = utils.get_current_time_millis()

    """
        METHODS
    """

    def render(self, screen, camera):
        self.head_member.render(screen, camera, self.world_x, self.world_y, 0)

        self.chest_member.render(screen, camera, 0, 0, 0)

        self.left_arm_member.render(screen, camera, 0, 0, utils.map(math.cos((utils.get_current_time_millis() - self.start_at) / 300), -1, 1, -3, 2))
        self.right_arm_member.render(screen, camera, 0, 0, utils.map(math.cos((utils.get_current_time_millis() - self.start_at) / 350), -1, 1, -3, 2))

        self.left_leg_member.render(screen, camera, 0, 0, 0)
        self.right_leg_member.render(screen, camera, 0, 0, 0)

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
