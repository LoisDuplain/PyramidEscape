from component.renderer.renderer import AnchorType
from entity.player.member.member import Member


class HeadMember(Member):
    def __init__(self):
        super().__init__(0, "player-head.png", AnchorType.BOTTOM_MIDDLE)