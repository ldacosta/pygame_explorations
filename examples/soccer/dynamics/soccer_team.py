#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from examples.soccer.dynamics.soccer_player import SoccerPlayer
from vector import Vec2d

class SoccerTeam(object):

    def __init__ (self, name: str, colour, num_players: int, soccer_field):

        self.name = name
        self.colour = colour
        self.players = []
        self.soccer_field = soccer_field

        random.seed()
        populated_regions = []

        for i in range (0, num_players):
            assigned_region = False
            # we don't 2 players on same region:
            while (not assigned_region):
                if (name == 'red'):
                    region = random.randint(0, 11)
                elif (name == 'blue'):
                    region = random.randint(16, 27)
                if not region in populated_regions:
                    assigned_region = True
            populated_regions.append(region)
                
            # La posición inicial es el centro de la región.
            pos = Vec2d(soccer_field.regions[region].rect.center)

            # Nuevo jugador.
            self.players.append(SoccerPlayer(name, colour, i, pos, soccer_field))

    def move_players(self):
        for player in self.players:
            player.move()