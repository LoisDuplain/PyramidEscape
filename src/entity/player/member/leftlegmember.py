from entity.player.member.member import Member
from component.renderer.renderer import AnchorType


class LeftLegMember(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-left-leg.png", AnchorType.TOP_MIDDLE, fixed_to)
        super().set_offset_x(-fixed_to.get_original_width() / 4)
        super().set_offset_y(fixed_to.get_original_height() / 2)