#!/usr/bin/python
# -*- coding: utf-8 -*-

from dynamics.particle import Particle
from vector import Vec2d
from examples.soccer.dynamics.SteeringBehaviours import SteeringBehaviours

class SoccerPlayer (Particle):

    def __init__ (self, team, colour, number, pos, soccer_field):

        super().__init__(pos, 15, Vec2d(0, 0), Vec2d(4, 4),
                              Vec2d(soccer_field.playing_area.center), 1)

        self.team = team
        self.colour = colour
        self.number = number
        self.initialPos = pos
        self.soccer_field = soccer_field
        self.direction = (soccer_field.playing_area.center - pos).normalized()

        self.steeringBehaviours = SteeringBehaviours(self, soccer_field.ball)

        self.steeringBehaviours.activated['arrive'] = True

    def reset (self, pos): # TODO: this parameter is not used.
        self.pos = self.initialPos

    def warm_up(self):
        """Runs back and forth between the ball and a random point in the field."""
        self.velocity = self.steeringBehaviours.calculate()
        self.pos += self.velocity
        self.pos = Vec2d(int(self.pos.x), int(self.pos.y))
        if not self.is_moving():
            if self.steeringBehaviours.target == self.soccer_field.ball.pos:
                # let's go back towards where I was.
                self.steeringBehaviours.target = self.initialPos
            else:
                # let's go towards the ball.
                self.steeringBehaviours.target = self.soccer_field.ball.pos
        self.direction = Vec2d(self.steeringBehaviours.target - self.pos).normalized()

    def move (self):
        self.warm_up()
