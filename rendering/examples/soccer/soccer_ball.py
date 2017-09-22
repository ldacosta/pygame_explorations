from pygame.color import THECOLORS

from rendering.base import DrawingObjects, DrawingCircle, Renderable
from soccer.soccer_ball import SoccerBall


class SoccerBallPygameRenderable(Renderable):

    def __init__(self, soccer_ball: SoccerBall):
        self.ball = soccer_ball
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[
                DrawingCircle(
                    center=self.ball.pos,
                    radius=self.ball.radius,
                    color=THECOLORS['black'],
                    line_thickness=2)],
            lines=[])
