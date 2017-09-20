import pygame
from pygame import Rect
from pygame.colordict import THECOLORS
from pygame import QUIT
import sys
from util.entity import MovingEntity
from vector import Vec2d

TOP_LEFT = (50, 50)
WIDTH_HEIGHT = (1050, 720)

class SoccerBall(MovingEntity):

    def __init__(self, pos: Vec2d, size: float, mass: float, velocity: float, soccer_field):
        super().__init__(
            pos=pos,
            radius=size,
            velocity=velocity,
            max_speed=velocity,
            heading=Vec2d(soccer_field.playing_area.center),
            mass=mass)

    def kick(self, direction: Vec2d, force: Vec2d):

        direction = direction.normalized()
        acceleration = (direction * force) / self.mass
        self.velocity = acceleration # TODO: ooooops <----------------- units don't match!!!!!!

class SoccerField(object):

    def __init__(self, width: int, height: int):

        self.width, self.height = width, height
        pygame.display.set_caption('Soccer Field')
        # where will I show the field:
        self.surface = pygame.display.set_mode((self.width, self.height), 0, 32)
        # actual playing field:
        self.playing_area = Rect(TOP_LEFT, WIDTH_HEIGHT)


        # "walls": side lines and lines at the end of the field
        # Used to detect when ball goes out of bound
        # TODO
        self.walls = []


    def render(self):
        """Renders the playing field."""

        self.surface.fill(THECOLORS['green'])
        pygame.draw.rect(self.surface, THECOLORS['white'], self.playing_area, 7)
        pygame.draw.circle(self.surface, THECOLORS['white'], self.playing_area.center, 10, 5)
        pygame.draw.circle(self.surface, THECOLORS['white'], self.playing_area.center, 75, 5)
        pygame.draw.line(self.surface, THECOLORS['white'], self.playing_area.midtop, self.playing_area.midbottom, 5)


if __name__ == "__main__":
    WIDTH, HEIGHT = 1200, 800
    FPS = 30

    pygame.init()

    clock = pygame.time.Clock()
    soccer_field = SoccerField(width=WIDTH, height=HEIGHT)

    while True:
        tick_time = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        soccer_field.render()

        pygame.display.update()
