from dynamics.entity import MovingEntity
from vector import Vec2d


class Particle(MovingEntity):

    def __init__(self,
                 pos: Vec2d,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):
        super().__init__(pos, radius, velocity, max_speed, heading, mass)

    def is_moving(self) -> bool:
        """Is this particle moving?"""
        return not (self.velocity == Vec2d(0,0))
