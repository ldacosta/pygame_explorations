from pygame.color import THECOLORS

from rendering.base import DrawingObjects, DrawingCircle, DrawingRect, Renderable
from soccer.soccer_region import SoccerRegion


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
