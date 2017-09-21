import abc

import pygame
from pygame.color import THECOLORS
from pygame.rect import Rect
from typing import List, Tuple

class DrawingRect(object):

    def __init__(self, shape: Rect, color, lines_thickness: int):
        self.shape = shape
        self.color = color
        self.lines_thickness = lines_thickness

class DrawingCircle(object):

    def __init__(self, center: float, radius: float, color, line_thickness: int = 2):
        self.center = center
        self.radius = radius
        self.color = color
        self.line_thickness = line_thickness

class DrawingLine(object):

    def __init__(self, begin: float, end: float, color, thickness: int = 2):
        self.begin = begin
        self.end = end
        self.color = color
        self.line_thickness = thickness

class DrawingObjects(object):

    def __init__(self, rects: List[DrawingRect], circles: List[DrawingCircle], lines: List[DrawingLine]):
        self.rects = rects
        self.circles = circles
        self.lines = lines

    def __add__(self, other):
        return DrawingObjects(
            rects = self.rects + other.rects,
            circles = self.circles + other.circles,
            lines=self.lines + other.lines)

def pygame_render(objects_to_draw: DrawingObjects, surface):
    for rect in objects_to_draw.rects:
        pygame.draw.rect(surface, rect.color, rect.shape, rect.lines_thickness)
    for circle in objects_to_draw.circles:
        pygame.draw.circle(surface, circle.color, circle.center, circle.radius, circle.line_thickness)
    for a_line in objects_to_draw.lines:
        pygame.draw.line(surface, a_line.color, a_line.begin, a_line.end, a_line.line_thickness)


class Renderable(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def representation(self) -> DrawingObjects:
        pass