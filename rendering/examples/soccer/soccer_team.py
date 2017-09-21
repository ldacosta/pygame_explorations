from functools import reduce

from rendering.base import Renderable, DrawingObjects
from rendering.examples.soccer.soccer_player import SoccerPlayerPygameRenderable
from soccer.soccer_team import SoccerTeam


class SoccerTeamPygameRenderable(Renderable):


    def __init__(self, team: SoccerTeam):
        self.team = team
        super().__init__()

    def representation(self) -> DrawingObjects:
        return reduce(
                    lambda repr_1, repr_2: repr_1 + repr_2,
                    map(lambda player: SoccerPlayerPygameRenderable(player).representation(), self.team.players))