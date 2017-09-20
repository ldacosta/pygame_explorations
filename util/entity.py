from vector import Vec2d

class MovingEntity(object):

    def __init__(self,
                 pos: Vec2d,
                 radius: float,
                 velocity: float,
                 max_speed: float,
                 heading: Vec2d,
                 mass: float):

        self.pos = pos
        self.radius = radius
        self.velocity = velocity
        self.max_speed = max_speed
        self.heading = heading
        # vector perpendicular to the place where I am heading:
        self.side = self.heading.perpendicular()
        self.mass = mass
