#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List
import pygame
from pygame.color import THECOLORS

from soccer import Wall2d
from vector import Vec2d
from dynamics.entity import Particle
from soccer import Global

# El balón es una entidad móvil.
class SoccerBall (Particle):

    def __init__(self, pos: Vec2d, size: float, mass: float, velocity: Vec2d, soccer_field):

        super().__init__(pos, size, velocity, velocity,
                              Vec2d(soccer_field.playing_area.center), mass)

        self.oldPos = pos
        
        self.soccer_field = soccer_field
        self.walls: List[Wall2d] = soccer_field.walls
        self.direction = Vec2d(0, 0)

    def testCollisionWithWalls (self):

        velNormal = Vec2d(self.velocity)
        
        # Iterar sobre todos los laterales del campo
        # para calcular si el balón interseca.
        for w in self.walls:
            if w.dist_to(self.pos) < Global.TOUCHLINE:
                self.reset(self.pos)

    # Golpea el balón en la dirección dada.
    def kick (self, direction, force):
        
        # Normaliza la dirección.
        direction = direction.normalized()
        # Calculo de la aceleración.
        acceleration = (direction * force) / self.mass
        # Actualiza la velocidad.
        self.velocity = acceleration

    # Devuelve la posición del balón en el futuro.
    def futurePosition (self, time):

        # u = velocidad de inicio.
        # Cálculo del vector ut.
        ut = self.velocity * time

        # Cálculo de 1/2*a*t*t, que es un escalar.
        half_a_t_squared = 0.5 * Global.FRICTION * time * time

        # Conversión del escalar a vector,
        # considerando la velocidad (dirección) de la bola.
        scalarToVector = half_a_t_squared * self.velocity.normalized()

        # La posición predicha es la actual
        # más la suma de los dos términos anteriores.
        return self.pos + ut + scalarToVector

    def move (self):

        self.oldPos = self.pos

        # Cálculo de colisiones.
        self.testCollisionWithWalls()

        # Cómputo de la fricción del campo sobre la bola.
        if self.velocity.get_length_sqrd() > Global.FRICTION ** 2:
            # Se actualiza la velocidad y la posición.
            self.velocity += (self.velocity.normalized() * Global.FRICTION)
            self.pos += self.velocity

            self.pos = Vec2d(int(self.pos.x), int(self.pos.y))

            self.heading = self.velocity.normalized()

    def render (self):

        # En cada instante de render se actualiza el estado del balón.
        self.move()

        pygame.draw.circle(self.soccer_field.surface, THECOLORS['black'], 
                           self.pos, self.radius, 0)