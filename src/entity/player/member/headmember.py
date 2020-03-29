from entity.player.member.member import Member
from component.renderer.renderer import AnchorType


class HeadMember(Member):
    def __init__(self):
        super().__init__(0, "player-head.png", AnchorType.BOTTOM_MIDDLE)