#!/usr/bin/python
# -*- coding: utf-8 -*-

from vector import Vec2d

class Wall2d:

    def __init__ (self, a: Vec2d, b: Vec2d):

        # Muro a-b
        # a <-------------------------------> b
        self.a = a
        self.b = b

        aux = Vec2d(b - a)
        aux = aux.normalized()
        self.normal = aux.perpendicular_normal()

    def dist_to(self, p: Vec2d) -> float:
        dotA = (p.x - self.a.x) * (self.b.x - self.a.x) + (p.y - self.a.y) * (self.b.y - self.a.y)

        if dotA <= 0:
            return self.a.get_distance(p)

        dotB = (p.x - self.b.x) * (self.a.x - self.b.x) + (p.y - self.b.y) * (self.a.y - self.b.y)

        if dotB <= 0:
            return self.b.get_distance(p)

        closest_point = self.a + ((self.b - self.a) * dotA) / (dotA + dotB)

        return p.get_distance(closest_point)
