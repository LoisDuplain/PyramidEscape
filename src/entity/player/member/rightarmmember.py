from component.renderer.renderer import AnchorType
from entity.player.member.member import Member


class RightArmMember(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-right-arm.png", AnchorType.TOP_LEFT, fixed_to)
        super().set_offset_x(fixed_to.get_original_width()/2)
        super().set_offset_y(-fixed_to.get_original_height() / 2 + 1)