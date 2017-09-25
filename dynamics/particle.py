# -*- coding: utf-8 -*-
"""A Particle.

TODO:

"""

from dynamics.entity import MovingEntity
from vector import Vec2d
from point import Point


class Particle(MovingEntity): # pylint: disable=too-few-public-methods

    def __init__(self,
                 pos: Point,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):
        super().__init__(pos, radius, velocity, max_speed, heading, mass)
