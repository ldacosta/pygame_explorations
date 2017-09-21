#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, random

from dynamics.entity import Particle
from soccer.SteeringBehaviours import *
from soccer import Global
from vector import Vec2d

# El jugador es una entidad móvil.
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

        # Controla el calentamiento del jugador.
        self.warmingUp = 0

    def reset (self, pos): # TODO: this parameter is not used.
        self.pos = self.initialPos

    # Calentamiento antes del partido ;-)
    def move (self):

        self.velocity = self.steeringBehaviours.calculate()
        
        self.pos += self.velocity
        self.pos = Vec2d(int(self.pos.x), int(self.pos.y))

        # Si llega a algún objetivo,
        # sigue 'corriendo'.
        if self.velocity == Vec2d(0, 0):
            if self.warmingUp == 0:
                # Vuelta a la posición inicial.
                self.steeringBehaviours.target = self.initialPos
                self.warmingUp = 1
            else:
                # Vuelta a la posición del balón.
                self.steeringBehaviours.target = self.soccer_field.ball.pos
                self.warmingUp = 0

        # Actualización del vector dirección.
        self.direction = Vec2d(self.steeringBehaviours.target - self.pos).normalized()

    def render (self):

        # En cada instante de render se actualiza el estado del jugador.
        self.move()

        pygame.draw.circle(self.soccer_field.surface, self.colour, 
                           self.pos, self.radius, 0)
        # Dibujar la dirección.
        pygame.draw.line(self.soccer_field.surface, self.colour, 
                           self.pos, self.pos + ((self.radius * 2) * self.direction))
