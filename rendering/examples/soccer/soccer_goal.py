from rendering.base import DrawingObjects, DrawingLine, Renderable
from soccer.soccer_goal import SoccerGoal


class SoccerGoalPygameRenderable(Renderable):

    def __init__(self, soccer_goal: SoccerGoal):
        self.goal = soccer_goal
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[],
            lines=[DrawingLine(
                begin=self.goal.leftPost,
                end=self.goal.rightPost,
                color=self.goal.colour,
                thickness=6)])