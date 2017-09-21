#!/usr/bin/python
# -*- coding: utf-8 -*-

from vector import Vec2d

class SoccerGoal:

    def __init__ (self, team, colour, position, soccer_field):

        self.team = team
        self.colour = colour
        self.soccer_field = soccer_field

        aux = self.soccer_field.playing_area.height / 6

        # Pósters izquierdo y derecho.
        self.leftPost = Vec2d(position - Vec2d(0, aux))
        self.rightPost = Vec2d(position + Vec2d(0, aux))
