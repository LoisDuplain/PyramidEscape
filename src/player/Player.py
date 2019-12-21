import Utils
from renderer.RenderableObject import RenderableObject
import math


class Member(RenderableObject):
    def __init__(self, character_velocity_remover, sprite):
        super().__init__(sprite)
        self.character_velocity_remover = character_velocity_remover

    def get_character_velocity_remover(self):
        return self.character_velocity_remover


class HeadMember(Member):
    def __init__(self):
        super().__init__(0, "player-head.png")


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.head_member = HeadMember()
        self.started_at = Utils.get_current_time_millis()

    def render(self, screen):
        self.head_member.render(screen, x=self.x, y=self.y, angle=Utils.map(math.cos(Utils.get_current_time_millis()/1000 - self.started_at/1000), -1, 1, 0, 720))
