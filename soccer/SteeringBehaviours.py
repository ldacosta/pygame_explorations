#!/usr/bin/python
# -*- coding: utf-8 -*-

# Deceleration factors.
SLOW = 3
NORMAL = 2
FAST = 1

from vector import Vec2d

class SteeringBehaviours:

    def __init__ (self, player, ball):

        self.player = player
        self.ball = ball

        self.target = Vec2d(ball.pos)

        # Comportamientos activados.
        self.activated = {}
        self.activated['seek'] = False
        self.activated['pursuit'] = False
        self.activated['arrive'] = False

    def calculate (self):

        steeringForce = self.sumForces()
        return steeringForce

    def sumForces (self):
        
        force = Vec2d(0, 0)

        if self.activated['seek']:
            force += self.seek(self.target)
        if self.activated['pursuit']:
            force += self.pursuit(self.target)
        if self.activated['arrive']:
            force += self.arrive(self.target)

        return force

    def truncate (self, max_force):
        
        if self.steeringForce > max_force:
            self.steeringForce = max_force

    # Dado un objetivo, este comportamiento devuelve la fuerza
    # que orienta al jugador hacia el objetivo y lo mueve.
    def seek (self, target):

        desiredVelocity = (target - self.player.pos).normalized()
        desiredVelocity *= self.player.max_speed

        return (desiredVelocity - self.player.velocity)

    # Similar a seek pero llegando con velocidad nula.
    def arrive (self, target, deceleration = FAST):

        toTarget = target - self.player.pos

        # Distancia al target.
        dist = toTarget.get_length()
        
        if (dist > 25):
            # Para ajustar la deceleración...
            decelerationTweaker = 3
            # Cálculo de la velocidad requerida.
            speed = dist / (deceleration * decelerationTweaker)

            speed = min(speed, self.player.max_speed.get_length())

            # Igual que seek...
            desiredVelocity = toTarget * speed / dist

            return desiredVelocity - self.player.velocity

        return Vec2d(0, 0)

    # Crea una fuerza que mueve al jugador hacia la bola.
    def pursuit (self, target):

        toBall = self.ball.pos - self.player.pos
        self.direction = toBall.normalized()
        lookAheadTime = 0.0

        if self.ball.velocity.get_length() != 0.0:
            lookAheadTime = toBall.get_length() / self.ball.velocity.get_length()

        # ¿Dónde estará la bola en el futuro?
        target = self.ball.futurePosition(lookAheadTime)

        return self.arrive(target)
        
