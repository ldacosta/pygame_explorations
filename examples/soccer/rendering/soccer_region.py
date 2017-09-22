from pygame.color import THECOLORS

from examples.soccer.dynamics.soccer_region import SoccerRegion
from rendering.base import DrawingObjects, DrawingRect, Renderable


class SoccerRegionPygameRenderable(Renderable):

    def __init__(self, soccer_region: SoccerRegion):
        self.region = soccer_region
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[
                DrawingRect(shape=self.region.rect, color=THECOLORS['white'], lines_thickness=1)
            ],
            circles=[],
            lines=[])
