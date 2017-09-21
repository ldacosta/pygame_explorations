
import abc
from vector import Vec2d

class Entity(object):

    def __init__(self, pos: Vec2d, radius: float, mass: float):
        self.pos = pos
        self.radius = radius
        self.mass = mass

class StaticEntity(Entity):

    def __init__(self, pos: Vec2d, radius: float, mass: float):
        super().__init__(pos, radius, mass)

class MovingEntity(Entity):

    def __init__(self,
                 pos: Vec2d,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):

        super().__init__(pos, radius, mass)
        self.velocity = velocity
        self.max_speed = max_speed
        self.heading = heading
        # vector perpendicular to the place where I am heading:
        self.side = self.heading.perpendicular()

    @abc.abstractmethod
    def move(self):
        pass

    def reset(self, pos):
        self.pos = pos
        self.velocity = Vec2d(0, 0)


class Particle(MovingEntity):

    def __init__(self,
                 pos: Vec2d,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):
        super().__init__(pos, radius, velocity, max_speed, heading, mass)

