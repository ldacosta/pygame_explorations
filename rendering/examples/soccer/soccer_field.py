from pygame.color import THECOLORS
from rendering.examples.soccer.soccer_goal import SoccerGoalPygameRenderable
from rendering.examples.soccer.soccer_team import SoccerTeamPygameRenderable
from rendering.examples.soccer.soccer_ball import SoccerBallPygameRenderable
from rendering.base import DrawingObjects, DrawingRect, DrawingCircle, DrawingLine, Renderable
from soccer.soccer_field import SoccerField


class SoccerFieldPygameRenderable(Renderable):

    def __init__(self, soccer_field: SoccerField):
        self.field = soccer_field
        super().__init__()

    def representation(self) -> DrawingObjects:
        field = DrawingObjects(
            rects=[
                DrawingRect(
                    shape=self.field.playing_area,
                    color=THECOLORS['white'],
                    lines_thickness=3)],
            circles=[
                DrawingCircle(
                    center=self.field.playing_area.center,
                    radius=10,
                    color=THECOLORS['white'],
                    line_thickness=2),
                DrawingCircle(
                    center=self.field.playing_area.center,
                    radius=75,
                    color=THECOLORS['white'],
                    line_thickness=2)],
            lines=[
                DrawingLine(
                    begin=self.field.playing_area.midtop,
                    end=self.field.playing_area.midbottom,
                    color=THECOLORS['white'],
                    thickness=2)])
        ball = SoccerBallPygameRenderable(soccer_ball=self.field.ball).representation()
        goal_1 = SoccerGoalPygameRenderable(soccer_goal=self.field.goals['red']).representation()
        goal_2 = SoccerGoalPygameRenderable(soccer_goal=self.field.goals['blue']).representation()
        team_1 = SoccerTeamPygameRenderable(team=self.field.teams['red']).representation()
        team_2 = SoccerTeamPygameRenderable(team=self.field.teams['blue']).representation()
        return field + ball + goal_1 + goal_2 + team_1 + team_2


