from rendering.base import Renderable, DrawingObjects, DrawingCircle, DrawingLine
from soccer.soccer_player import SoccerPlayer


class SoccerPlayerPygameRenderable(Renderable):

    def __init__(self, soccer_player: SoccerPlayer):
        self.player = soccer_player
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[ # actual position
                DrawingCircle(
                    center=self.player.pos,
                    radius=self.player.radius,
                    color=self.player.colour,
                    line_thickness=0)],
            lines=[ # direction
                DrawingLine(
                    begin=self.player.pos,
                    end=self.player.pos + ((self.player.radius * 2) * self.player.direction),
                    color=self.player.colour,
                    thickness=6)])