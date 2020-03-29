from component.renderer.renderer import AnchorType
from entity.player.member.member import Member


class LeftArmMember(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-left-arm.png", AnchorType.TOP_RIGHT, fixed_to)
        super().set_offset_x(-fixed_to.get_original_width() / 2 + 1)
        super().set_offset_y(-fixed_to.get_original_height() / 2 + 1)