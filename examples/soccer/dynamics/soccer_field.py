#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Rect  # TODO: we have to get rid of this
from pygame.color import THECOLORS  # TODO: we have to get rid of this
from examples.soccer.dynamics import Global
from examples.soccer.dynamics.Wall2d import Wall2d
from examples.soccer.dynamics.soccer_ball import SoccerBall
from examples.soccer.dynamics.soccer_goal import SoccerGoal
from examples.soccer.dynamics.soccer_team import SoccerTeam

from examples.soccer.dynamics.soccer_region import SoccerRegion
from vector import Vec2d


class SoccerField(object):

    def __init__ (self, name: str):

        self.name = name

        # Terreno real de juego.
        self.playing_area = Rect(Global.TOP_LEFT, Global.WIDTH_HEIGHT)

        # Walls para detectar cuándo el balón sale del terreno de juego.
        self.walls = []

        top_left = Vec2d(self.playing_area.topleft)
        top_right = Vec2d(self.playing_area.topright)
        bottom_left = Vec2d(self.playing_area.bottomleft)
        bottom_right = Vec2d(self.playing_area.bottomright)

        self.walls.append(Wall2d(top_left, top_right))
        self.walls.append(Wall2d(top_right, bottom_right))
        self.walls.append(Wall2d(top_left, bottom_left))
        self.walls.append(Wall2d(bottom_left, bottom_right))

        # Zonas importantes en el campo.
        self.regions = {}
        for i in range (0, 7):
            for j in range (0, 4):
                id = i * 4 + j
                rect = Rect(50 + i * 150, 50 + j * 180, 150, 180)
                self.regions[id] = SoccerRegion(id, rect, self)

        # Balón.
        self.ball = SoccerBall(pos = Vec2d(self.playing_area.center), size=10, mass=2,
                               velocity=Vec2d(1, 10), soccer_field=self)
        # Equipos
        self.teams = {}
        self.teams['red'] = SoccerTeam('red', THECOLORS['red'], 4, self)
        self.teams['blue'] = SoccerTeam('blue', THECOLORS['blue'], 4, self)

        # Porterías.
        self.goals = {}
        self.goals['red'] = SoccerGoal('red', THECOLORS['red'], self.playing_area.midleft, self)
        self.goals['blue'] = SoccerGoal('blue', THECOLORS['blue'], self.playing_area.midright, self)

    def update_states(self):
        self.ball.move()
        self.teams['red'].move_players()
        self.teams['blue'].move_players()
