from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape) :

        def __init__(self, x, y, radius) :
                super().__init__(x, y, radius)

        def draw(self, screen) :
                pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

        def update(self, dt) :
                self.position += self.velocity * dt

		def split(self, dt) :
			self.kill()
			if ASTEROID_MIN_RADIUS >= self.radius : return
			randAngle = random.uniform(20,50)
			firstVelocity,secondVelocity = self.velocity.rotate(randAngle), self.velocity.rotate((-1)*randAngle)
			firstSplit, secondSplit = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS),Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
			firstSplit.velocity, secondSplit.velocity = firstVelocity * 1.2, secondVelocity * 1.2
