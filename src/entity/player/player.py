import math

import utils
from component.renderer.renderer import AnchorType
from entity.entity import Entity
from entity.player.chestpart import ChestPart
from entity.player.headpart import HeadPart
from entity.player.leftarmpart import LeftArmPart
from entity.player.leftlegpart import LeftLegPart
from entity.player.rightarmpart import RightArmPart
from entity.player.rightlegpart import RightLegPart


class Player(Entity):

    def __init__(self):
        super().__init__()

        self.head_part = HeadPart()

        self.chest_part = ChestPart()
        self.chest_part.set_anchor(AnchorType.TOP_MIDDLE)
        self.chest_part.set_offset_y(15)

        self.left_arm_part = LeftArmPart()
        self.left_arm_part.set_anchor(AnchorType.TOP_RIGHT)
        self.left_arm_part.set_offset_x(-15)

        self.right_arm_part = RightArmPart()
        self.right_arm_part.set_anchor(AnchorType.TOP_LEFT)
        self.right_arm_part.set_offset_x(15)

        self.left_leg_part = LeftLegPart()
        self.left_leg_part.set_anchor(AnchorType.TOP_MIDDLE)
        self.left_leg_part.set_offset_x(-7.5)
        self.left_leg_part.set_offset_y(50)

        self.right_leg_part = RightLegPart()
        self.right_leg_part.set_anchor(AnchorType.TOP_MIDDLE)
        self.right_leg_part.set_offset_x(7.5)
        self.right_leg_part.set_offset_y(50)

        self.head_part.add_child(self.chest_part)

        self.chest_part.add_child(self.left_arm_part)
        self.chest_part.add_child(self.right_arm_part)
        self.chest_part.add_child(self.left_leg_part)
        self.chest_part.add_child(self.right_leg_part)

        super().add_part(self.head_part)

    def update(self, delta_time, keys):
        self.left_arm_part.set_angle(utils.map(math.cos((utils.get_current_time_millis()) / 300), -1, 1, -3, 2))
        self.right_arm_part.set_angle(utils.map(math.cos((utils.get_current_time_millis()) / 350), -1, 1, -3, 2))
