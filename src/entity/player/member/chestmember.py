from component.renderer.renderer import AnchorType
from entity.player.member.member import Member


class ChestMember(Member):
    def __init__(self, fixed_to):
        super().__init__(0, "player-chest.png", AnchorType.MIDDLE, fixed_to)
        super().set_offset_y(25)